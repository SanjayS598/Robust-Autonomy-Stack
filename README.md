# Robust Autonomy Stack

**Self-Healing Autonomous Driving with Learned Risk Monitoring and RL Red-Teaming**

A complete autonomous driving stack built on MetaDrive that includes:
- Full autonomy pipeline: CV world model → tracking → prediction → planning → control
- ML-based failure risk estimator that triggers safe degradation modes
- RL adversary for automated scenario generation and edge case discovery
- Reproducible evaluation suite with robustness analysis
- Cross-platform: Works on Mac (ARM/Intel), Linux, and Windows

## Features

- **Self-healing autonomy**: Automatically switches to cautious mode or minimal-risk condition when failure risk is high
- **Learned risk monitoring**: Supervised ML model predicts imminent failures based on stack health signals
- **RL red-teaming**: Adversarial agent discovers hard scenarios (cut-ins, aggressive drivers, sensor failures)
- **Full reproducibility**: YAML-based scenarios with seeds for deterministic replay
- **Modular design**: Clean separation of perception, planning, control, and safety layers
- **Cross-platform**: Pure Python implementation works on any OS including Apple Silicon Macs

## Getting Started

### Prerequisites

- Python 3.9+ 
- Works on any platform: macOS (Intel/Apple Silicon), Linux, Windows

### Installation

1. **Clone and setup**
   ```bash
   git clone <your-repo-url>
   cd Robust-Autonomy-Stack
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   pip install metadrive-simulator
   ```

3. **Test MetaDrive installation**
   ```bash
   python test_metadrive_connection.py
   ```

4. **Run your first scenario** (coming in Phase 2+)
   ```bash
   python -m robust_autonomy_stack.cli run --scenario scenarios/examples/cut_in.yaml
   ```

## Development Roadmap

- [x] Phase 0: Project scaffolding and configuration system
- [x] Phase 1: Simulator selection and setup (switched from CARLA to MetaDrive for cross-platform support)
- [ ] Phase 2: CV world model (camera-based perception, lane detection, freespace)
- [ ] Phase 3: Tracking and prediction with uncertainty
- [ ] Phase 4: Planning and control
- [ ] Phase 5: ML risk model and safety supervisor
- [ ] Phase 6: RL adversarial scenario generator
- [ ] Phase 7: Evaluation framework and reporting

## Why MetaDrive?

We use MetaDrive simulator instead of CARLA because:
- **Cross-platform**: Pure Python, works on any OS including Apple Silicon Macs
- **Lightweight**: Faster iteration and development
- **RL-native**: Built-in Gymnasium interface, designed for reinforcement learning
- **Pip-installable**: No Docker or binary dependencies
- **Procedural scenarios**: Perfect for automated adversarial testing

The novel contributions (self-healing autonomy, risk ML, RL adversary) are simulator-agnostic.

## License

MIT License - see [LICENSE](LICENSE) for details
