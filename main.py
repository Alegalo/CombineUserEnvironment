# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 20:27:03 2022

@author: alegal
"""

import matplotlib.pyplot as plt
from user_env import UserEnv


TIMESTEPS = 1000 
env = UserEnv(NAME="user1", N_ACTIONS=5, RAND_INFLUENCE=0.05, 
              NOISE_LEVEL=0.1, seed=10)

obs = env.reset()

for i in range(TIMESTEPS):
    
    action = 0
    
    reward = env.step(0)
    
    

env.render()
    
    
    


