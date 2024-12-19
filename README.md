# System Performance Monitor

A lightweight, user-friendly system monitoring tool built specifically for macOS that helps track system resource usage with explicit user consent and local data storage.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.6+-green.svg)
![Platform](https://img.shields.io/badge/platform-macOS-lightgrey.svg)

## Features

- Real-time monitoring of:
  - CPU usage
  - Memory usage
  - Disk usage
- Data visualization with live updates
- Local data storage in macOS standard directories
- CSV export functionality
- Privacy-focused with explicit user consent
- Persistent settings
- Comprehensive logging

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
```
2. Install required packages:
```bash
pip3 install psutil
```
3. Run
```bash
python3 main.py
```
All monitoring data is stored locally in:
```bash
~/Library/Logs/SystemMonitor/
```

## Privacy

This application:
- Stores all data locally on your machine
- Requires explicit user consent before monitoring
- Does not send any data over the network
- Allows full control over monitored resources
- Provides easy data cleanup options
