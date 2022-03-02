# CombineUserEnvironment
Custom environment following the gym api. Used in the paper "A New Bandit Setting Balancing Information from State Evolution and Corrupted Context"

## Usage

from user_env import UserEnv

env = UserEnv(NAME="pat1", N_ACTIONS=5, NOISE_LEVEL=1.0, ACTION_INFLUENCE=0.001, RAND_INFLUENCE=0.01, NOISE_FEATURE=False,
                  BEST_ACTION_FEATURE=False)



