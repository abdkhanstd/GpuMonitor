
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
```

## Configuration

- `GPUS_PER_ROW`: Number of GPUs displayed per row.
- `BAR_LENGTH`: Length of the progress bars.
- `CRITICAL_TEMP`: Temperature considered critical.
- `MEMORY_USER_LIMIT`: Number of top memory-using processes to show.

## Installation

You can install the `GpuMonitor` package directly from PyPI:

```bash
pip install gpumon
```

Alternatively, you can install it directly from the GitHub repository:

```bash
pip install git+https://github.com/abdkhanstd/GpuMonitor.git
```

## Usage

Run the script using the following command after installation:

```bash
gpumon
```

Or, if you are running the script directly:

```bash
python gpumon.py
```

## Example Output

Here is an example output for a system with 8 NVIDIA A100 GPUs, each with 80 GB of RAM:

```
GPU0 NVIDIA A100    Temp: 55C [████░░] Load: 70% [██████░] Mem: 64000/81920 MB [██████░] Freq: 1500/1800 MHz [█████░]
GPU1 NVIDIA A100    Temp: 53C [███░░░] Load: 60% [████░░░] Mem: 50000/81920 MB [████░░░] Freq: 1450/1800 MHz [████░░]
GPU2 NVIDIA A100    Temp: 50C [███░░░] Load: 50% [███░░░░] Mem: 45000/81920 MB [████░░░] Freq: 1400/1800 MHz [███░░░]
GPU3 NVIDIA A100    Temp: 48C [██░░░░] Load: 40% [██░░░░░] Mem: 30000/81920 MB [██░░░░░] Freq: 1350/1800 MHz [██░░░░]
GPU4 NVIDIA A100    Temp: 45C [██░░░░] Load: 30% [█░░░░░░] Mem: 25000/81920 MB [█░░░░░░] Freq: 1300/1800 MHz [█░░░░░]
GPU5 NVIDIA A100    Temp: 43C [█░░░░░] Load: 20% [░░░░░░░] Mem: 15000/81920 MB [░░░░░░░] Freq: 1250/1800 MHz [░░░░░░]
GPU6 NVIDIA A100    Temp: 40C [█░░░░░] Load: 10% [░░░░░░░] Mem: 10000/81920 MB [░░░░░░░] Freq: 1200/1800 MHz [░░░░░░]
GPU7 NVIDIA A100    Temp: 38C [░░░░░░] Load:  5% [░░░░░░░] Mem:  5000/81920 MB [░░░░░░░] Freq: 1150/1800 MHz [░░░░░░]
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
