# CombineUserEnvironment
Custom environment following the gym api. Used in the paper "A New Bandit Setting Balancing Information from State Evolution and Corrupted Context".
Make sure to have installed gym:

```
pip install gym

```

## Usage

### Creating a user environment
```python

from user_env import UserEnv
env = UserEnv(NAME="pat1", N_ACTIONS=5, NOISE_LEVEL=1.0, , RAND_INFLUENCE=0.01, seed=42)
```

If no RAND_INFLUENCE is specified, a standard value of 0.05 is set. RAND_INFLUENCE is the parameter c in the paper.

### Run simulation

```python
TIMESTEPS = 1000 #define the number of timesteps

for i in range(TIMESTEPS):
  #choose action using policy
  action = 0 # As an example use action 0 for all times
  reward = env.step(action)
  #use reward to update policy, the example has a constant policy so we do not update!
  
 ```
 
 ### Plotting state, actions and rewards over time
 The environment contains a memory that can be accessed to show the state, actions and reward over time. The render() method
 returns the memory as well as plots the contents using matplotlib.
 
 ```python
 
    state, reward, actions = env.render()
 
 ```
 
 OR directly access the memory
 
  
 ```python
 
    state, reward, actions = env.state_history, env.reward_history, env.actions
 
 ```
 
 
  


