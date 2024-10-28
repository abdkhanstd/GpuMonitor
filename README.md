# GPU Monitor (`gpumon`)

`gpumon` is a real-time GPU monitoring tool designed to display various metrics for NVIDIA GPUs, including temperature, fan speed, memory usage, load, and power consumption. It provides color-coded output for easy identification of critical values and can operate in both continuous and one-time monitoring modes.

## Features

- **Real-time Monitoring**: Continuously monitors NVIDIA GPU statistics.
- **Detailed Metrics**: Displays temperature, fan speed, memory usage, GPU load, and power consumption.
- **Color-Coded Output**: Highlights different levels of each metric with distinct colors for easy visualization.
- **Customizable**: Users can adjust the bar length and refresh rate.
- **Single or Continuous Mode**: Option to display GPU status once or continuously update.

## Installation

### Prerequisites

- **Python 3.x**
- **NVIDIA drivers**
- **`nvidia-smi` command-line utility**

### Install using pip

To install `gpumon`, use the following command:

```bash
pip install gpumon
```

## Usage

Run the tool using the command line:

### Continuous Monitoring (default mode)

```bash
gpumon
```

This command will start `gpumon` in continuous monitoring mode, refreshing the display every 0.5 seconds.

### One-Time Status Display

To display the GPU status once and then exit:

```bash
gpumon --continuous False
```

### Custom Bar Length and Refresh Rate

You can customize the appearance and behavior of the monitoring display:

```bash
gpumon --bar-length 5 --refresh-rate 1.0
```

- `--bar-length`: Sets the length of the progress bars (default is 5).
- `--refresh-rate`: Sets the refresh rate in seconds (default is 0.5 seconds).

### Command-Line Arguments

- `--bar-length`: The length of the progress bars. This controls how much detail is displayed in the bar representation.
- `--refresh-rate`: The rate in seconds at which the display refreshes.
- `--continuous`: Set to `False` for a one-time status display, otherwise the tool runs continuously (default is `True`).

## Example Output

```

[0]-NVIDIA RTX A6000 Fan:  30% Power: 107.31 W Temp:  53C [███░░] Load:   3% [░░░░░] Mem:  9265/49140 MB [█░░░░] Freq: 1920/2100 MHz [█████]
[1]-NVIDIA RTX A6000 Fan:  34% Power: 112.09 W Temp:  62C [███░░] Load:   4% [░░░░░] Mem:  4607/49140 MB [░░░░░] Freq: 1905/2100 MHz [█████]
[2]-NVIDIA RTX A6000 Fan:  36% Power: 120.68 W Temp:  64C [███░░] Load:   4% [░░░░░] Mem:  4607/49140 MB [░░░░░] Freq: 1890/2100 MHz [████░]
[3]-NVIDIA RTX A6000 Fan:  30% Power: 104.77 W Temp:  58C [███░░] Load:   4% [░░░░░] Mem:  4583/49140 MB [░░░░░] Freq: 1905/2100 MHz [█████]
[4]-NVIDIA RTX A6000 Fan:  30% Power:  99.32 W Temp:  58C [███░░] Load:   2% [░░░░░] Mem:  4583/49140 MB [░░░░░] Freq: 1920/2100 MHz [█████]
[5]-NVIDIA RTX A6000 Fan:  35% Power: 101.68 W Temp:  64C [███░░] Load:   1% [░░░░░] Mem:  4521/49140 MB [░░░░░] Freq: 1890/2100 MHz [████░]
[6]-NVIDIA RTX A6000 Fan:  34% Power:  96.49 W Temp:  62C [███░░] Load:   4% [░░░░░] Mem:  4607/49140 MB [░░░░░] Freq: 1875/2100 MHz [████░]
[7]-NVIDIA RTX A6000 Fan:  30% Power: 106.99 W Temp:  56C [███░░] Load:   4% [░░░░░] Mem:  4497/49140 MB [░░░░░] Freq: 1905/2100 MHz [█████]

```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Notes

- Ensure that the `nvidia-smi` tool is available on your system, as `gpumon` relies on it to gather GPU metrics.


