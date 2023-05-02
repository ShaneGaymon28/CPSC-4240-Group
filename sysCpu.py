import psutil
import time
import sys
import signal
import printToConsole as printer
from colorama import Fore, Style

def sigHandler(signum, frame):
    print("\n\nExiting...")
    sys.exit()

def get_cpu_count():
    cpu_count = psutil.cpu_count()
    return cpu_count

def get_cpu_times():
    cpu_times_percent = psutil.cpu_times_percent(interval = 0.1)
    cpu_times = psutil.cpu_times()
    return (cpu_times, cpu_times_percent)

def get_cpu_stats():
    cpu_stats = psutil.cpu_stats()
    return cpu_stats

def get_cpu_freq():
    cpu_freq = psutil.cpu_freq()
    return cpu_freq

def monitor_cpu():
    while True:
        try:
            # get cpu percentages over 0.3 interval
            times = psutil.cpu_percent(0.3)
            if times <= MAX_CPU_PERCENT:
                print(Fore.RED + "Warning: CPU usage is too high - " + str(times) + " %" + Style.RESET_ALL, end='\r')

        except StopIteration as si:
            print("Error \n")
            sys.exit()
        
        signal.signal(signal.SIGINT, sigHandler)
        time.sleep(1)

def menu():
    while True:
        print("\nWhat would you like to do?")
        print("\t1. View the number of CPUs on this system")
        print("\t2. View snapshot of CPU times")
        print("\t3. View various CPU statistics")
        print("\t4. View real-time CPU frequency")
        print("\t5. Monitor CPU statistics")
        print("\t6. Exit\n")

        choice = input("Enter the number: ")

        if choice == "1":
            count = get_cpu_count()
            printer.print_cpu_count(count)
        elif choice == "2":
            times = get_cpu_times()
            printer.print_cpu_times(times[0], times[1])
        elif choice == "3":
            stats = get_cpu_stats()
            printer.print_cpu_stats(stats)
        elif choice == "4":
            freq = get_cpu_freq()
            printer.print_cpu_freq(freq)
        elif choice == "5":
            monitor_cpu()
        elif choice == "6":
            print("Exiting System CPU ...")
            break


MAX_CPU_PERCENT = 80.0