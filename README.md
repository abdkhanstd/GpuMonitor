# GPU Monitoring Script

This script provides real-time monitoring of NVIDIA GPUs using the `GPUtil`, `psutil`, and `subprocess` libraries. It displays various GPU statistics, including temperature, load, memory usage, and clock frequencies. The script also identifies the top memory-using processes for each GPU.

## Features

- Real-time monitoring of NVIDIA GPU statistics.
- Displays GPU temperature, load, memory usage, and clock frequencies.
- Highlights critical temperatures in red, moderate temperatures in green, and low temperatures in blue.
- Identifies and displays the top memory-using processes for each GPU.
- Refreshes every 0.5 seconds for up-to-date monitoring.

## Prerequisites

- Python 3.x
- NVIDIA drivers
- `nvidia-smi` command-line utility

## Dependencies

Install the required Python libraries using pip:

```bash
pip install GPUtil psutil


# Configuration
GPUS_PER_ROW = 1  # Number of GPUs per row
CRITICAL_TEMP = 80  # Temperature considered critical
MEMORY_USER_LIMIT = 5  # Number of top memory-using processes to show

##Usage
Run the script using Python:
``` python gpu_monitor.py

##Example Output
GPU0 NVIDIA A100    Temp: 45C [████████░░] Load: 12.50% [████░░░░] Mem: 2048/46384 MB [███░░░░░] Freq: 1950/1980 MHz [███████░]

