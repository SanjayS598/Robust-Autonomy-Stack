#!/usr/bin/env python3
import sys
print("Starting MetaDrive test...", flush=True)

try:
    print("Importing...", flush=True)
    from metadrive import MetaDriveEnv
    print("SUCCESS: Imported MetaDrive", flush=True)
    
    print("Creating environment...", flush=True)
    env = MetaDriveEnv({"use_render": False, "manual_control": False})
    print("SUCCESS: Created environment", flush=True)
    
    print("Resetting environment...", flush=True)
    obs, info = env.reset()
    print(f"SUCCESS: Reset complete, obs shape={obs.shape}", flush=True)
    
    print("Taking 3 steps...", flush=True)
    for i in range(3):
        action = env.action_space.sample()
        obs, reward, terminated, truncated, info = env.step(action)
        print(f"Step {i+1}: OK", flush=True)
    
    env.close()
    print("\n=== ALL TESTS PASSED ===", flush=True)
    
except Exception as e:
    print(f"\n=== ERROR: {e} ===", flush=True)
    import traceback
    traceback.print_exc()
    sys.exit(1)
