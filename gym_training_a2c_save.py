import gym
from stable_baselines3 import A2C
import os

models_dir = "models/A2C"
logdir = "logs"

if not os.path.exists(models_dir):
    os.makedirs(models_dir)

if not os.path.exists(logdir):
    os.makedirs(logdir)

env = gym.make('LunarLander-v2')
env.reset()

model = A2C('MlpPolicy', env, verbose=1, tensorboard_log=logdir)

TIME_STEPS = 10000
iters = 0
for i in range(30):
    iters += 1
    model.learn(total_timesteps=TIME_STEPS, reset_num_timesteps=False, tb_log_name="A2C")
    model.save(f"{models_dir}/{TIME_STEPS * iters}")

env.close()
