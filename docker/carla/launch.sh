#!/bin/bash
# CARLA server launch script with low-fidelity, headless settings
# This script is used inside the CARLA container

# Launch CARLA with optimal settings for headless development
./CarlaUE4.sh \
  -RenderOffScreen \
  -quality-level=Low \
  -nosound \
  -carla-rpc-port=2000 \
  -carla-streaming-port=2001
