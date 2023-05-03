import sys

def print_cpu_count(cpu_count):
    print("\nCPU Count: " + str(cpu_count))

def print_cpu_times(cpu_times, cpu_times_percent):
    print("CPU Times: ")
    print("\tUser: " + str(cpu_times[0]) + " (" + str(cpu_times_percent[0]) + "%)")
    print("\tSystem: " + str(cpu_times[2]) + " (" + str(cpu_times_percent[2]) + "%)")
    print("\tIdle: " + str(cpu_times[3]) + " (" + str(cpu_times_percent[3]) + "%)")
    print("\tIO Wait: " + str(cpu_times[4]) + " (" + str(cpu_times_percent[4]) + "%)")

def print_cpu_stats(cpu_stats):
    print("CPU Stats: ")
    print("\tContext Switches: " + str(cpu_stats[0]))
    print("\tInterrupts: " + str(cpu_stats[1]))
    print("\tSoft Interrupts: " + str(cpu_stats[2]))
    print("\tSystem calls: " + str(cpu_stats[3]))

def print_cpu_freq(cpu_freq):
    print("CPU Frequency: ")
    print("\tCurrent: " + str(cpu_freq[0]))
    print("\tMin: " + str(cpu_freq[1]))
    print("\tMax: " + str(cpu_freq[2]))

def print_virtual_memory(virtual_memory):
    print("\nVirtual Memory: ")
    print("\tTotal: " + str(round(virtual_memory[0]/1024/1024, 2)) + " MB")
    print("\tAvailable: " + str(round(virtual_memory[1]/1024/1024, 2)) + " MB")
    print("\tPercentage: " + str(virtual_memory[2]) + " %")
    print("\tUsed: " + str(round(virtual_memory[3]/1024/1024, 2)) + " MB")
    print("\tActive: " + str(round(virtual_memory[5]/1024/1024, 2)) + " MB")
    print("\tInactive: " + str(round(virtual_memory[6]/1024/1024, 2)) + " MB")
    print("\tCached: " + str(round(virtual_memory[8]/1024/1024, 2)) + " MB")

def print_swap_memory(swap_memory):
    print("\nSwap Memory: ")
    print("\tTotal: " + str(round(swap_memory[0]/1024/1024, 2)) + " MB")
    print("\tUsed: " + str(round(swap_memory[1]/1024/1024, 2)) + " MB")
    print("\tFree: " + str(round(swap_memory[2]/1024/1024, 2)) + " MB")
    print("\tPercentage: " + str(round(swap_memory[3]/1024/1024, 2)) + " MB")

def print_disk_partitions(disk_partitions):
    num_partitions = len(disk_partitions)
    cur_partition_num = 1
    print("\nDisk Partitions: ")
    for x in range(num_partitions):
        print("\t" + str(cur_partition_num) + ". " + str(disk_partitions[x][0]))
        print("\t\tMount Point: " + str(disk_partitions[x][1]))
        cur_partition_num += 1

def print_disk_usage(disk_usage, path):
    print("\nDisk Usage for " + path)
    print("\tTotal: " + str(round(disk_usage[0]/1024/1024, 2)) + " MB")
    print("\tUsed: " + str(round(disk_usage[1]/1024/1024, 2)) + " MB")
    print("\tFree: " + str(round(disk_usage[2]/1024/1024, 2)) + " MB")
    print("\tPercentage: " + str(disk_usage[3]) + " %")

def print_disk_io(disk_io):
    print("\nDisk I/O Statistics: ")
    print("\t# Reads: " + str(disk_io[0]))
    print("\t# Writes: " + str(disk_io[1]))
    print("\tBytes read: " + str(disk_io[2]) + " bytes (" + str(round(disk_io[2]/1024/1024, 2)) + " MB)")
    print("\tBytes written: " + str(disk_io[3]) + " bytes (" + str(round(disk_io[3]/1024/1024, 2)) + " MB)")
