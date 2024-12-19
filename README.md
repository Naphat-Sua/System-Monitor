# System-Monitor

A lightweight, user-friendly system monitoring tool built specifically for macOS that helps track system resource usage with explicit user consent and local data storage.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.6+-green.svg)
![Platform](https://img.shields.io/badge/platform-macOS-lightgrey.svg)

## Features

- 🖥️ Real-time monitoring of:
  - CPU usage
  - Memory usage
  - Disk usage
- 📊 Data visualization with live updates
- 💾 Local data storage in macOS standard directories
- 📈 CSV export functionality
- 🔒 Privacy-focused with explicit user consent
- ⚙️ Persistent settings
- 📝 Comprehensive logging

## Requirements

- macOS 10.12 or later
- Python 3.6+
- Required packages:
  - `psutil`
  - `tkinter` (usually comes with Python)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/naphat-sua/system-monitor.git

cd system-monitor

pip3 install psutil
