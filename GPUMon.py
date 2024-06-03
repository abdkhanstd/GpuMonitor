import os
import GPUtil
import time
import subprocess
import re
import psutil

# Configuration
#os.environ["CUDA_VISIBLE_DEVICES"] = "1"  # Specify the GPU IDs to use
GPUS_PER_ROW = 1  # Number of GPUs per row
CRITICAL_TEMP = 80  # Temperature considered critical
MEMORY_USER_LIMIT = 5  # Number of top memory-using processes to show

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

def get_top_memory_users(gpu_id):
    command = f"nvidia-smi pmon -i {gpu_id} -c 1"
    try:
        output = subprocess.check_output(command.split()).decode()
        users = []
        lines = output.strip().split('\n')[2:]  # Skip headers
        for line in lines:
            details = line.split()
            if len(details) >= 4:
                pid, type, gpu_mem_usage = int(details[1]), details[2], int(details[3])
                if pid > 0 and gpu_mem_usage > 0:
                    process = psutil.Process(pid)
                    users.append((process.name(), gpu_mem_usage))
        users.sort(key=lambda x: x[1], reverse=True)
        return users[:MEMORY_USER_LIMIT]
    except Exception as e:
        print("Error fetching top memory users:", e)
        return []

def print_progress_bar(percentage, max_value=100, bar_length=8, bar_character='█', empty_character='░', color='\033[92m'):
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

def print_gpu_stats(gpu, current_freq, max_freq):
    temp_color = get_color_code(gpu.temperature)

    temp_bar = print_progress_bar(gpu.temperature, max_value=100, color=temp_color)
    load_bar = print_progress_bar(gpu.load * 100, color=temp_color)
    mem_bar = print_progress_bar((gpu.memoryUsed / gpu.memoryTotal) * 100, color=temp_color)
    freq_bar = print_progress_bar(current_freq, max_freq, color=temp_color)

    print(f"\033[93mGPU{gpu.id}\033[0m \033[93m{gpu.name[:12]:<12}\033[0m Temp: {gpu.temperature}C [{temp_bar}] Load: {gpu.load * 100:.2f}% [{load_bar}] Mem: {gpu.memoryUsed}/{gpu.memoryTotal} MB [{mem_bar}] Freq: {current_freq}/{max_freq} MHz [{freq_bar}]", end=' ')

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
        print_gpu_stats(gpu, current_freq, max_freq)
        gpu_count += 1
        if gpu_count % GPUS_PER_ROW == 0:
            print()
    if gpu_count % GPUS_PER_ROW != 0:
        print()
    lines_to_move_up = (gpu_count // GPUS_PER_ROW + (1 if gpu_count % GPUS_PER_ROW > 0 else 0)) * 1  # Adjust based on the output complexity
    first_run = False
    time.sleep(0.5)  # Refresh rate, increased to 0.
