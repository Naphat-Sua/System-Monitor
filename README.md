# MacBook System Performance Monitor 🖥️📊

A Python-based real-time system monitoring tool for macOS that tracks key performance metrics including CPU, memory, disk, network, battery, and temperature.

## Features

- **Comprehensive Monitoring**:
  - CPU Usage (total and per-core)
  - Memory (RAM) utilization
  - Disk space usage
  - Network bandwidth (upload/download)
  - Battery status and power state
  - CPU temperature (requires optional tools)

- **User-Friendly Interface**:
  - Clean terminal-based display
  - Auto-refreshing output
  - Human-readable units
  - Color-coded percentages (optional)

- **Advanced Functionality**:
  - Configurable update interval
  - Cross-platform core functionality (macOS focus)
  - Expandable architecture for custom metrics

## Installation

```bash
# Clone repository
git clone https://github.com/naphat-sua/system-monitor.git
cd macbook-system-monitor

# Install dependencies
pip install psutil

# Optional temperature monitoring tools
brew install osx-cpu-temp  # or gem install iStats
