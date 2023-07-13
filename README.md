# Banking Project

This project is a simple banking system that allows you to manage clients, their balances, and transfers. It uses a JSON file to store the clients' data and Python to perform the operations.

## Files

The project consists of three files:

⦁
clients.json: This file contains the list of clients and their details, such as id, name, date of birth, balance, and VIP status. Each client is represented by a JSON object inside an array called "clients".

⦁
banking_1.py: This file contains the functions that perform the core logic of the banking system, such as loading and saving clients, adding, updating, deleting, displaying, transferring, and making VIP clients.

⦁
banking_2.py: This file contains the main function that runs the user interface of the banking system. It displays a menu with options to choose from and calls the functions from banking_1.py accordingly.

## How to run

To run the project, open a terminal or command prompt and navigate to the folder where the project files are located. Then type:
python banking_2.py

This will start the program and display the menu with options. You can enter your choice by typing a number and pressing enter. You can exit the program by choosing option 0.

## Example output

Here is an example of how the program works:
1. Add new client
2. Update existing client
3. Delete client
4. Display clients
5. Display total balance and total number of clients
6. Make transfer
7. Make client VIP
0. Exit

Select your option: 4

Enter the clients ID: 3

ID:  3

Name:  Nizar

Date of Birth:  1996-06-27

Age:  27

Balance:  49999991989878.0

Client displayed successfully.

1. Add new client
2. Update existing client
3. Delete client
4. Display clients
5. Display total balance and total number of clients
6. Make transfer
7. Make client VIP
0. Exit

Select your option: 6

Enter the sender ID: 3

Enter the receiver ID: 2

Enter the amount: 10000

Transfer made successfully.

1. Add new client
2. Update existing client
3. Delete client
4. Display clients
5. Display total balance and total number of clients
6. Make transfer
7. Make client VIP
0. Exit

Select your option: 5

Total money in the bank:  49999992007878.0

Total number of clients:  5

1. Add new client
2. Update existing client
3. Delete client
4. Display clients
5. Display total balance and total number of clients
6. Make transfer
7. Make client VIP
0. Exit

Select your option: 0

Exiting...
