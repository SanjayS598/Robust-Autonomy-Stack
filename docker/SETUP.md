# CARLA Setup and Testing Guide

## Important Note for Apple Silicon (M1/M2/M3/M4) Macs

**CARLA does not currently support ARM64 architecture.** The Docker images are x86_64 only, and CARLA's Unreal Engine binary cannot be emulated on ARM Macs (causes "Illegal instruction" errors).

### Options for Apple Silicon Users:

1. **Use a Linux VM or remote server** (Recommended)
   - Run CARLA on a Linux machine (x86_64)
   - Connect your Python client from Mac over network
   - Update `CARLA_HOST` environment variable to point to remote server

2. **Use GitHub Codespaces or Cloud Development**
   - Develop and run everything in cloud (x86_64 VMs)
   - Access via browser or VS Code Remote

3. **Dual-boot Linux or use Parallels/UTM with x86_64 Linux**
   - Not recommended due to performance overhead

### For Intel Mac or Linux Users

Continue with the instructions below.

## Starting CARLA Server

```bash
# Start CARLA server (headless, low-fidelity)
docker compose up carla-server

# Or run in background
docker compose up -d carla-server
```

Wait 30-60 seconds for the server to fully initialize. You'll see logs indicating the server is ready.

## Testing the Connection

### Option 1: Using Docker client container (recommended for Mac)

```bash
# Build the client container (first time only)
docker compose build client

# Run the connection test
docker compose run --rm client python test_carla_connection.py
```

### Option 2: From your local Python (Linux only)

If you're on Linux and have CARLA Python API installed locally:

```bash
python test_carla_connection.py
```

## Expected Output

```
Attempting to connect to CARLA server at localhost:2000...
Connected to CARLA server version: 0.9.15
Current map: Town01
Available maps (8):
   - /Game/Carla/Maps/Town01
   - /Game/Carla/Maps/Town02
   - /Game/Carla/Maps/Town03
   ...
   
CARLA server is running and accessible!
```

## Running Your Autonomy Stack

Once the server is running and connection test passes:

```bash
# Run a scenario
docker compose run --rm client python -m carla_robust_autonomy_stack.cli run --scenario scenarios/examples/cut_in.yaml

# Or enter the container interactively
docker compose run --rm client bash
```

## Troubleshooting

### Server won't start
- Check Docker has enough resources (4GB RAM minimum, 8GB recommended)
- View logs: `docker compose logs carla-server`
- Try restarting: `docker compose restart carla-server`

### Connection timeouts
- Server takes 30-60 seconds to start
- Ensure ports 2000-2001 aren't blocked
- Check server health: `docker compose ps`

### Performance issues
- CARLA is resource-intensive even in low-quality mode
- Close other applications
- Reduce resource limits in compose.yml if needed

## Stopping Everything

```bash
# Stop all services
docker compose down

# Stop and remove volumes
docker compose down -v
```
