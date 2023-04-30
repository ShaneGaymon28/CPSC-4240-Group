import sys
import appUsage
import sysCpu
import sysMem

def app_menu():
    while True:
        print("Welcome!\n")
        print("\t1. Application Monitor")
        print("\t2. System CPU Monitor")
        print("\t3. System Memory Monitor")
        print("\t4. Exit\n")

        choice = input("Enter the number: ")

        if choice == "1":
            # figure something out for this
            appUsage.monitor_cpu("atom", 50, 80)
        elif choice == "2":
            sysCpu.menu()
        elif choice == "3":
            sysMem.menu()
        elif choice == "4":
            print("Exiting app...")
            break

app_menu()
