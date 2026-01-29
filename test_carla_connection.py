# Test script to verify CARLA server connection
# Run this to check if CARLA server is accessible

import sys
import time

try:
    import carla
except ImportError:
    print("ERROR: CARLA Python API not found")
    print("Run this script inside the Docker client container:")
    print("  docker compose run --rm client python test_carla_connection.py")
    sys.exit(1)

def test_connection():
    print("Attempting to connect to CARLA server at localhost:2000...")
    
    try:
        # Connect to CARLA server
        client = carla.Client('carla-server', 2000)
        client.set_timeout(10.0)
        
        # Get server version
        version = client.get_server_version()
        print(f"SUCCESS: Connected to CARLA server version: {version}")
        
        # Get current world
        world = client.get_world()
        map_name = world.get_map().name
        print(f"Current map: {map_name}")
        
        # Get available maps
        available_maps = client.get_available_maps()
        print(f"Available maps ({len(available_maps)}):")
        for m in available_maps[:5]:  # Show first 5
            print(f"   - {m}")
        
        print("\nSUCCESS: CARLA server is running and accessible!")
        return True
        
    except Exception as e:
        print(f"ERROR: Connection failed: {e}")
        print("\nTroubleshooting:")
        print("1. Ensure CARLA server is running: docker compose up carla-server")
        print("2. Wait 30-60 seconds for server to fully start")
        print("3. Check server logs: docker compose logs carla-server")
        return False

if __name__ == "__main__":
    success = test_connection()
    sys.exit(0 if success else 1)
