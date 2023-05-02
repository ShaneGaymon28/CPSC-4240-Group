import psutil
import time
import sys
import signal
import printToConsole as printer
from colorama import Fore, Style

def sigHandler(signum, frame):
    print("\n\nExiting...")
    sys.exit()

def get_virtual_memory():
    virtual_memory = psutil.virtual_memory()
    return virtual_memory

def get_swap():
    swap_memory = psutil.swap_memory()
    return swap_memory

def get_disk_partitions():
    disk_partitions = psutil.disk_partitions()
    return disk_partitions

def get_disk_usage():
    get_disk_partitions()
    path = input("\nEnter the Path of the Partition: ")
    try:
        disk_usage = psutil.disk_usage(path)

    except OSError:
        print("Invalid path - Exiting...")
        sys.exit()

    return (disk_usage, path)

def get_disk_io():
    disk_io = psutil.disk_io_counters()
    return disk_io


def monitor_memory():
    num_iterations = 1
    total_time = 0
    while True:
        try:
            vm = get_virtual_memory()
            swap = get_swap()            
            
            if vm[2] >= MAX_VM_PERCENT:
                print(Fore.RED + "Warning: Virtual Memory usage is too high - ")
                printer.print_virtual_memory(vm)
                print(Style.RESET_ALL, end='\r')

            if swap[3] >= MAX_SWAP_PERCENT:
                print(Fore.RED + "Warning: Swap Memory usage is too high - ")
                printer.print_swap_memory(swap)
                print(Style.RESET_ALL, end='\r')            

        except StopIteration:
            print("\nError...")
            sys.exit()

        signal.signal(signal.SIGINT, sigHandler)
        time.sleep(1)
        num_iterations += 1
        total_time += 1


def menu():
    while True:
        print("\nWhat would you like to do? ")
        print("\t1. View System-Wide Virtual Memory Statistics")
        print("\t2. View System-Wide Swap Memory Statistics")
        print("\t3. View Disk Partitions")
        print("\t4. View Usage Information for a Disk Partition")
        print("\t5. View System-Wide Disk I/O Statistics")
        print("\t6. Monitor System-Wide Statistics")
        print("\t7. Exit\n")

        choice = input("Enter the number: ")

        if choice == "1":
            vm = get_virtual_memory()
            printer.print_virtual_memory(vm)
        elif choice == "2":
            swap = get_swap()
            printer.print_swap_memory(swap)
        elif choice == "3":
            dp = get_disk_partitions()
            printer.print_disk_partitions(dp)
        elif choice == "4":
            du = get_disk_usage() # change to ask user in function for path
            printer.print_disk_usage(du[0], du[1])
        elif choice == "5":
            io = get_disk_io()
            printer.print_disk_io(io)
        elif choice == "6":
            monitor_memory()
        elif choice == "7":
            print("Exiting System Memory ...")
            break


MAX_VM_PERCENT = 85.0
MAX_SWAP_PERCENT = 75.0
