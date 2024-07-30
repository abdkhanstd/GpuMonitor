import os
import subprocess
import sys
import time
import re
import psutil

# Check for GPUtil and install if not found
try:
    import GPUtil
except ImportError:
    print("GPUtil not found. Installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "gputil"])
    import GPUtil

# Configuration
os.environ["CUDA_VISIBLE_DEVICES"] = "1"  # Specify the GPU IDs to use
GPUS_PER_ROW = 1  # Number of GPUs per row
CRITICAL_TEMP = 80  # Temperature considered critical
MEMORY_USER_LIMIT = 5  # Number of top memory-using processes to show
BAR_LENGTH = 6  # Reduced bar length

def move_cursor_up(lines):
    print(f"\033[{lines}A", end='')

def get_gpu_clock_frequencies(gpu_id):
    try:
        output = subprocess.check_output(["nvidia-smi", "-i", str(gpu_id), "--query-gpu=clocks.gr,clocks.max.gr", "--format=csv,noheader,nounits"]).decode()
        current_freq, max_freq = map(int, re.findall(r'\d+', output))
        return current_freq, max_freq
    except Exception as e:
        print("Error fetching GPU clock frequencies:", e)
        return 0, 0

def get_gpu_fan_speed(gpu_id):
    try:
        output = subprocess.check_output(["nvidia-smi", "-i", str(gpu_id), "--query-gpu=fan.speed", "--format=csv,noheader,nounits"]).decode().strip()
        fan_speed = int(re.findall(r'\d+', output)[0])
        return fan_speed
    except Exception as e:
        print("Error fetching GPU fan speed:", e)
        return 0

def print_progress_bar(percentage, max_value=100, bar_length=BAR_LENGTH, bar_character='█', empty_character='░', color='\033[92m'):
    filled_length = int(round(bar_length * percentage / float(max_value)))
    bar = bar_character * filled_length + empty_character * (bar_length - filled_length)
    return color + bar + '\033[0m'

def get_color_code(temperature):
    if temperature < 50:
        return '\033[94m'  # Blue
    elif temperature < 70:
        return '\033[92m'  # Green
    else:
        return '\033[91m'  # Red

def print_gpu_stats(gpu, current_freq, max_freq, fan_speed):
    temp_color = get_color_code(gpu.temperature)

    temp_bar = print_progress_bar(gpu.temperature, max_value=100, color=temp_color)
    load_bar = print_progress_bar(gpu.load * 100, color=temp_color)
    mem_bar = print_progress_bar((gpu.memoryUsed / gpu.memoryTotal) * 100, color=temp_color)
    freq_bar = print_progress_bar(current_freq, max_freq, color=temp_color)
    fan_bar = print_progress_bar(fan_speed, max_value=100, color=temp_color)

    print(f"\033[93mGPU{gpu.id}\033[0m \033[93m{gpu.name:<25}\033[0m Temp: {int(gpu.temperature):>3}C [{temp_bar}] Load: {int(gpu.load * 100):>3}% [{load_bar}] Mem: {int(gpu.memoryUsed):>5}/{int(gpu.memoryTotal):<5} MB [{mem_bar}] Freq: {int(current_freq):>4}/{int(max_freq):<4} MHz [{freq_bar}] Fan: {fan_speed:>3}% [{fan_bar}]", end=' ')

first_run = True
lines_to_move_up = 0

while True:
    gpus = GPUtil.getGPUs()
    if not first_run:
        move_cursor_up(lines_to_move_up)
    lines_to_move_up = 0
    gpu_count = 0
    for gpu in gpus:
        current_freq, max_freq = get_gpu_clock_frequencies(gpu.id)
        fan_speed = get_gpu_fan_speed(gpu.id)
        print_gpu_stats(gpu, current_freq, max_freq, fan_speed)
        gpu_count += 1
        if gpu_count % GPUS_PER_ROW == 0:
            print()
    if gpu_count % GPUS_PER_ROW != 0:
        print()
    lines_to_move_up = (gpu_count // GPUS_PER_ROW + (1 if gpu_count % GPUS_PER_ROW > 0 else 0)) * 1  # Adjust based on the output complexity
    first_run = False
    time.sleep(0.5)  # Refresh rate
