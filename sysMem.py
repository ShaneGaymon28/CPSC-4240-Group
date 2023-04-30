import psutil
import time
import sys
import signal

def sigHandler(signum, frame):
    print("\n\nExiting...")
    sys.exit()

def get_virtual_memory():
    virtual_memory = psutil.virtual_memory()
    print("\nVirtual Memory: ")
    print("\tTotal: " + str(round(virtual_memory[0]/1024/1024, 2)) + " MB")
    print("\tAvailable: " + str(round(virtual_memory[1]/1024/1024, 2)) + " MB")
    print("\tPercentage: " + str(virtual_memory[2]) + " %")
    print("\tUsed: " + str(round(virtual_memory[3]/1024/1024, 2)) + " MB")
    print("\tActive: " + str(round(virtual_memory[5]/1024/1024, 2)) + " MB")
    print("\tInactive: " + str(round(virtual_memory[6]/1024/1024, 2)) + " MB")
    print("\tCached: " + str(round(virtual_memory[8]/1024/1024, 2)) + " MB") 

def get_swap():
    swap_memory = psutil.swap_memory()
    print("\nSwap Memory: ")
    print("\tTotal: " + str(round(swap_memory[0]/1024/1024, 2)) + " MB")
    print("\tUsed: " + str(round(swap_memory[1]/1024/1024, 2)) + " MB")
    print("\tFree: " + str(round(swap_memory[2]/1024/1024, 2)) + " MB")
    print("\tPercentage: " + str(round(swap_memory[3]/1024/1024, 2)) + " MB")

def get_disk_partitions():
    disk_partitions = psutil.disk_partitions()
    num_partitions = len(disk_partitions)
    cur_partition_num = 1
    print("\nDisk Partitions: ")
    for x in range(num_partitions):
        print("\t" + str(cur_partition_num) + ". " + str(disk_partitions[x][0]))
        print("\t\tMount Point: " + str(disk_partitions[x][1]))
        cur_partition_num += 1

def get_disk_usage():
    get_disk_partitions()
    path = input("\nEnter the Path of the Partition: ")
    try:
        disk_usage = psutil.disk_usage(path)
        print("\nDisk Usage for " + path)
        print("\tTotal: " + str(round(disk_usage[0]/1024/1024, 2)) + " MB")
        print("\tUsed: " + str(round(disk_usage[1]/1024/1024, 2)) + " MB")
        print("\tFree: " + str(round(disk_usage[2]/1024/1024, 2)) + " MB")
        print("\tPercentage: " + str(disk_usage[3]) + " %")

    except OSError:
        print("Invalid path - Exiting...")
        sys.exit()

def get_disk_io():
    disk_io = psutil.disk_io_counters()
    print("\nDisk I/O Statistics: ")
    print("\t# Reads: " + str(disk_io[0]))
    print("\t# Writes: " + str(disk_io[1]))
    print("\tBytes read: " + str(disk_io[2]) + " bytes (" + str(round(disk_io[2]/1024/1024, 2)) + " MB)")
    print("\tBytes written: " + str(disk_io[3]) + " bytes (" + str(round(disk_io[3]/1024/1024, 2)) + " MB)")


def monitor_memory():
    num_iterations = 1
    total_time = 0
    while True:
        try:
            print("\nIteration #" + str(num_iterations))
            print("Elapsed Time: " + str(total_time) + " seconds")

            get_virtual_memory()
            get_swap()
            get_disk_io()            

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
            get_virtual_memory()
        elif choice == "2":
            get_swap()
        elif choice == "3":
            get_disk_partitions()
        elif choice == "4":
            get_disk_usage() # change to ask user in function for path
        elif choice == "5":
            get_disk_io()
        elif choice == "6":
            monitor_memory()
        elif choice == "7":
            print("Exiting System Memory ...")
            break


#menu()
