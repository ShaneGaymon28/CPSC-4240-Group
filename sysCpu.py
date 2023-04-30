import psutil
import time
import sys
import signal

def sigHandler(signum, frame):
    print("\n\nExiting...")
    sys.exit()

def get_cpu_count():
    cpu_count = psutil.cpu_count()
    print("\nCPU Count: " + str(cpu_count))

def get_cpu_times():
    cpu_times_percent = psutil.cpu_times_percent()
    cpu_times = psutil.cpu_times()
    print("CPU Times: ")
    print("\tUser: " + str(cpu_times[0]) + "(" + str(cpu_times_percent[0]) + "%)")
    print("\tSystem: " + str(cpu_times[2]) + "(" + str(cpu_times_percent[2]) + "%)")
    print("\tIdle: " + str(cpu_times[3]) + "(" + str(cpu_times_percent[3]) + "%)")
    print("\tIO Wait: " + str(cpu_times[4]) + "(" + str(cpu_times_percent[4]) + "%)")

def get_cpu_stats():
    cpu_stats = psutil.cpu_stats()
    print("CPU Stats: ")
    print("\tContext Switches: " + str(cpu_stats[0]))
    print("\tInterrupts: " + str(cpu_stats[1]))
    print("\tSoft Interrupts: " + str(cpu_stats[2]))
    print("\nSystem calls: " + str(cpu_stats[3]))

def get_cpu_freq():
    cpu_freq = psutil.cpu_freq()
    print("CPU Frequency: ")
    print("\tCurrent: " + str(cpu_freq[0]))
    print("\tMin: " + str(cpu_freq[1]))
    print("\tMax: " + str(cpu_freq[2]))

def monitor_cpu():
    while True:
        try:
            get_cpu_times()
            get_cpu_stats()
            get_cpu_freq()         

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
            get_cpu_count()
        elif choice == "2":
            get_cpu_times()
        elif choice == "3":
            get_cpu_stats()
        elif choice == "4":
            get_cpu_freq()
        elif choice == "5":
            monitor_cpu()
        elif choice == "6":
            print("Exiting System CPU ...")
            break


#menu()