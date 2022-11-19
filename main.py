import gym

# Create the environment
env = gym.make('LunarLander-v2', render_mode='human')

# required before you can step the environment
env.reset()

# sample action
# print("sample action:", env.action_space.sample())

# observation space shape:
# print("observation space shape: ", env.observation_space.shape)

# sample observation
# print("sample observation: ", env.observation_space.sample())

for step in range(200):
    env.render()
    obs, reward, done, trunc, info = env.step(env.action_space.sample())
    print(reward, done)

env.close()
