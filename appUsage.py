import psutil
import time
import sys
from colorama import Fore, Style

def monitor_usage(app_name, cpu_threshold, memory_threshold):
    while True:
        try:
            process = next(process for process in psutil.process_iter() if process.name() == app_name)
            cpu_usage = process.cpu_percent()
            memory_usage = process.memory_percent()

            if cpu_usage > cpu_threshold:
                print(Fore.RED + "Warning: CPU usage too high - " + str(cpu_usage) + "%" + Style.RESET_ALL, end='\r')

            if memory_usage > memory_threshold:
                print(Fore.RED + "Warning: Memory usage too high - " + str(memory_usage) + "%" + Style.RESET_ALL, end='\r')

            print("CPU usage: " + str(cpu_usage) + "%" + " | " + "Memory usage: " + str(memory_usage) + "%" , end='\r')

            exit_code = input("\ntype exit to quit\n")
            if exit_code == "exit":
                sys.exit()


        except StopIteration:
            print("Error: " + app_name + " not found.")
            sys.exit()

        time.sleep(1)

if __name__ == "__main__":
    monitor_usage("atom", 50, 80)
