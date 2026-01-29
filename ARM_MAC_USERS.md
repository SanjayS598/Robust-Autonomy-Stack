# Apple Silicon (ARM) Mac Users - Important Note

## The Problem

CARLA simulator is built on Unreal Engine and only provides x86_64 (Intel/AMD) binaries. Docker Desktop on Apple Silicon Macs can emulate x86_64, but CARLA's complex binary with CPU-specific instructions fails with "Illegal instruction" errors.

## Solutions

### Option 1: Run CARLA on a Remote Linux Server (Recommended)

1. **Set up a Linux machine** (AWS EC2, DigitalOcean, local Linux machine, etc.)
   ```bash
   # On the Linux server
   git clone <your-repo>
   cd Carla-Robust-Autonomy-Stack
   docker compose -f docker/compose.yml up -d carla-server
   ```

2. **From your Mac**, connect by updating the host:
   ```bash
   # Set CARLA_HOST to your server's IP
   export CARLA_HOST=<server-ip-address>
   
   # Run your client locally or in container
   python test_carla_connection.py
   ```

### Option 2: GitHub Codespaces (Cloud Development)

1. Open your repo in GitHub Codespaces
2. Codespaces runs on x86_64 Linux VMs
3. Develop and test entirely in the browser/VS Code Remote

### Option 3: Use Parallels/UTM with x86_64 Linux

1. Install Parallels Desktop or UTM
2. Create an x86_64 (not ARM) Linux VM
3. Enable Rosetta 2 emulation
4. Run Docker inside the VM

**Note**: This has significant performance overhead.

## Verification

To check if CARLA will work on your system:

```bash
# Check your architecture
uname -m
# If output is "arm64" or "aarch64" -> CARLA won't work natively
# If output is "x86_64" or "amd64" -> You're good to go
```

## Our Testing Approach

For this project development, we recommend:
- Develop code on your Mac (code is portable)
- Test/run on a Linux machine (local or cloud)
- CI/CD pipeline will run on x86_64 Linux for automated testing

This is a common pattern in robotics/simulation development where compute-heavy simulators run on servers.
