# CARLA Robust Autonomy Stack

**Self-Healing Autonomous Driving with Learned Risk Monitoring and RL Red-Teaming**

A complete autonomous driving stack for CARLA that includes:
- Full autonomy pipeline: CV world model → tracking → prediction → planning → control
- ML-based failure risk estimator that triggers safe degradation modes
- RL adversary for automated scenario generation and edge case discovery
- Reproducible evaluation suite with robustness analysis

## Features

- **Self-healing autonomy**: Automatically switches to cautious mode or minimal-risk condition when failure risk is high
- **Learned risk monitoring**: Supervised ML model predicts imminent failures based on stack health signals
- **RL red-teaming**: Adversarial agent discovers hard scenarios (cut-ins, weather, sensor dropouts)
- **Full reproducibility**: YAML-based scenarios with seeds for deterministic replay
- **Modular design**: Clean separation of perception, planning, control, and safety layers



## Current Progress

- Work in Progress

## License

MIT License - see [LICENSE](LICENSE) for details
Reproducible CARLA autonomy full-stack with a CV world model, a learned failure-risk supervisor for safe degradation, and an automated scenario generator for edge-case discovery with benchmark reports and replays.
