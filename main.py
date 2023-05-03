import sys
import appUsage
import sysCpu
import sysMem

def app_menu():
    while True:
        print("Welcome!\n")
        print("\t1. Application Monitor")
        print("\t2. System CPU Stats")
        print("\t3. System Memory Stats")
        print("\t4. Exit\n")

        choice = input("Enter the number: ")

        if choice == "1":
            app = input("Enter the application name: ")
            appUsage.monitor_usage(app, 50, 80)
        elif choice == "2":
            sysCpu.menu() # show the system cpu stats menu
        elif choice == "3":
            sysMem.menu() # show the system memory stats menu
        elif choice == "4":
            print("Exiting app...")
            break

app_menu()
