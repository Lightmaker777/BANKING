import banking_1 as banking
import re

def main():
    while True:
        print("1. Add new client")
        print("2. Update existing client")
        print("3. Delete client")
        print("4. Display clients")
        print("5. Display total balance and total number of clients")
        print("6. Make transfer")
        print("7. Make client VIP")
        print("0. Exit")
        try:            
            choice = int(input('\nSelect your option: '))
        except ValueError:
            print("Invalid option. Please try again.")
            print()
            continue
        print()
        # check choice
        if choice == 1:
            # add new client name
            while True:
                name = input("Enter new client name: ")[:20]  # Limit the name to 20 characters
                if not re.match("^[a-zA-Z\s]+$", name):
                    print("Invalid input. Client name should only contain letters and spaces.")
                    print()
                    continue

                dob = input("Enter new client date of birth (YYYY-MM-DD): ")
                if not re.match("^(\d{4})-(\d{2})-(\d{2})$", dob):
                    print("Invalid input. Date of birth should be in the format YYYY-MM-DD.")
                    print()
                    continue

                balance_input = input("Enter new client balance: ")
                if not balance_input.isdigit():
                    print("Invalid input. Balance should be a numeric value.")
                    print()
                    continue

                balance = float(balance_input)
                print()
                break  # Break out of the loop if all inputs are valid          
        elif choice == 2:
            # update client
            try:
                id = int(input("Enter client ID: "))
                name = input(
                    "Enter new client name (leave blank to keep old value): ")
                dob = input(
                    "Enter new client date of birth (YYYY-MM-DD)(leave blank to keep old value): ")
                balance_input = input(
                    "Enter new client balance (leave blank to keep old value): ")

                if balance_input.strip() == '':
                    balance = None
                else:
                    balance = float(balance_input)
                banking.update_clients(
                    banking.load_clients(), id, name, dob, balance)
                print()
            except ValueError:
                print("Invalid ID. Please try again.")
                print()

        elif choice == 3:
            # delete client
            try:                
                id = int(input("Enter client ID: "))
                banking.delete_clients(banking.load_clients(), id)
                print()
            except ValueError:
                print("Invalid ID. Please try again.")
                print()
        elif choice == 4:
            # display clients
            try:
                id = int(input("Enter the clients ID: "))
                banking.display_clients(banking.load_clients(), id)
                print()
            except ValueError:
                print("Invalid ID. Please try again.")
                print()
        elif choice == 5:
            # display total balance
            banking.display_total(banking.load_clients())
            print()
        elif choice == 6:
            # make transfer
            try:
                sender_id = int(input("Enter the sender ID: "))
                receiver_id = int(input("Enter the receiver ID: "))
                amount = float(input("Enter the amount: "))
                banking.make_transfer(banking.load_clients(),
                                    sender_id, receiver_id, amount)
                print()
            except ValueError:
                print("Invalid ID. Please try again.")
                print()
        elif choice == 7:
            # make client VIP
            try:
                id = int(input("Enter the client ID: "))
                banking.make_vip(banking.load_clients(), id)
                print()
            except ValueError:
                print("Invalid ID. Please try again.")
                print()
        elif choice == 0:
            # exit
            banking.save_clients(banking.load_clients())
            print("Exiting...")
            print()
            break
        else:
            # Invalid option
            print("Invalid option. Please try again.")
            print()


main()
