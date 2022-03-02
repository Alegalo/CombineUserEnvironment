# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 14:28:21 2021

@author: Alexander
"""
import gym
import numpy as np
import matplotlib.pyplot as plt
from gym import spaces
from gym.utils import seeding


class UserEnv(gym.Env):
    """Custom Environment that follows gym interface"""
    metadata = {'render.modes': ['human']}

    def __init__(self, NAME, N_ACTIONS, 
                 RAND_INFLUENCE=None, 
                 NOISE_LEVEL=0.0,
                 seed=None):
      super(UserEnv, self).__init__()
      self.action_space = spaces.Discrete(N_ACTIONS)
      self.observation_space = spaces.Box(0,1,(1,N_ACTIONS))
      self.viewer = None
      self.noise_level = NOISE_LEVEL

      if RAND_INFLUENCE is None:
          self.rand_inf = 0.05
      else:
          self.rand_inf = RAND_INFLUENCE
      
      self.name = NAME
      self.state = np.random.rand()
      self.state_history = [self.state]
      self.reward_history = []
      self.action_history = []
      self.action_order = None
      
      delta = 1.0/N_ACTIONS
      self.bins = delta*np.arange(N_ACTIONS+2)+delta
      self.action_order = np.arange(N_ACTIONS)
      self.np_random = None
      self.seed(seed)
    
    def _custom_clip(self, val):
          if val < 0.0: return 0
          if val > 1.0: return 1.0
          return val
      
    def step(self, action):
      
      if action == self.action_order[np.searchsorted(self.bins, self.state, side="left")]:
          reward = 1
      else:
          reward = 0
      
      #random influence
      
      self.state += ((-1.0)**self.np_random.binomial(1, 0.5))*self.rand_inf
      self.state = self._custom_clip(self.state)
      s_ = np.zeros(self.action_space.n)

      if self.np_random.rand() > self.noise_level:
          s_[np.searchsorted(self.bins, self.state, side="left")] = 1
      else:
          s_[np.searchsorted(self.bins, self.np_random.rand(), side="left")] = 1


      observation = np.array([s_])
      
      done = False
      
      #book keeping
      self.state_history.append(self.state)
      self.reward_history.append(reward)
      self.action_history.append(action)
      
      info = {}
      
      return observation, reward, done, info
      
      
    def reset(self):
      
      self.state = self.w_t[0]
      self.state_history = [self.state]
      self.reward_history = []
      self.action_history = []

      observation = np.zeros(self.action_space.n)

      if self.np_random.rand() > self.noise_level:
          observation[np.searchsorted(self.bins, self.state, side="left")] = 1
      else:
          observation[np.searchsorted(self.bins, self.np_random.rand(), side="left")] = 1
        
      return np.array([observation])  # reward, done, info can't be included
      
    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]
      
      
    def render(self, mode='rgb_array'):
      
        if mode =='rgb_array':
            plt.plot(self.state_history)
            plt.title("State")
            plt.figure()
            plt.plot(self.reward_history)
            plt.title("Rewards")
            plt.figure()
            plt.plot(self.action_history)
            plt.title("Actions")
            return [self.state_history, self.reward_history, self.action_history]
        else:
            raise NotImplementedError
      
      
      
    def close (self):
        if self.viewer is not None:
              self.viewer.close()
              self.viewer = None
