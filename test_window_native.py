# Test window creation in native terminal (outside VS Code)

from metadrive import MetaDriveEnv

config = {
    'use_render': True,
    'map': 'S',
}

print('Creating MetaDrive environment with rendering...')
env = MetaDriveEnv(config)
print('Calling reset...')
obs, info = env.reset()
print('SUCCESS! Window opened')
print('Taking 10 steps...')
for i in range(10):
    obs, reward, terminated, truncated, info = env.step([0.0, 0.5])
    if terminated or truncated:
        break
print('Done')
env.close()
