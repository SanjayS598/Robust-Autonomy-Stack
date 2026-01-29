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

## Development Status

- Phase 0: Project scaffolding [COMPLETE]
- Phase 1: MetaDrive integration [COMPLETE]
- Phase 2-7: In progress

## Getting Started

### Prerequisites

- **Python 3.11** (MetaDrive requires Python >=3.6,<3.12)
- Conda (recommended) or Python 3.11 virtual environment
- macOS, Linux, or Windows

### Installation

1. **Create a conda environment with Python 3.11:**
   ```bash
   conda create -n metadrive python=3.11 -y
   conda activate metadrive
   ```

2. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/Robust-Autonomy-Stack.git
   cd Robust-Autonomy-Stack
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Verify installation:**
   ```bash
   python test_simple.py
   ```

   You should see:
   ```
   Starting MetaDrive test...
   Importing...
   SUCCESS: Imported MetaDrive
   Creating environment...
   SUCCESS: Created environment
   ...
   === ALL TESTS PASSED ===
   ```

### Quick Start

Run a simple autonomous driving scenario:
```bash
python -m robust_autonomy_stack.cli run --config configs/default.yaml
```

Run the benchmark suite:
```bash
python -m robust_autonomy_stack.cli benchmark --config configs/benchmark.yaml
```



## License

MIT License - see [LICENSE](LICENSE) for details

