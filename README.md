# Banking Project
Welcome to the **Banking project**! This project provides a set of functionalities to manage client information and perform various banking operations. It includes two Python files: `banking_1.py` and `banking_2.py`. The `clients.json` file contains the initial data of the clients.
## Features
- Add new clients with their name, date of birth, and initial balance.
- Update existing client information including name, date of birth, and balance.
- Delete a client from the system.
- Display client details including ID, name, date of birth, age, and balance.
- Display the total balance and the total number of clients in the bank.
- Perform money transfers between clients.
- Make a client a VIP if their balance exceeds 10,000 euros.
## File Descriptions
### `clients.json`
This JSON file contains the initial data of the clients. It includes a list of client objects, where each object represents a client and contains the following attributes:
- `id`: Unique identifier for the client.
- `name`: Name of the client.
- `dob`: Date of birth of the client in the format YYYY-MM-DD.
- `balance`: Current balance of the client.
- `VIP` (optional): Boolean value indicating if the client is a VIP.
### `banking_1.py`
This file provides functions to load, save, and manipulate client data. It includes the following functions:
- `load_clients()`: Loads the list of clients from the `clients.json` file.
- `save_clients(clients)`: Saves the updated list of clients to the `clients.json` file.
- `get_age(dob)`: Calculates the age of a client based on their date of birth.
- `add_clients(clients, name, dob, balance)`: Adds a new client to the list of clients.
- `update_clients(clients, id, name=None, dob=None, balance=None)`: Updates the information of an existing client.
- `delete_clients(clients, id)`: Deletes a client from the list of clients.
- `display_clients(clients, id)`: Displays the details of a specific client.
- `display_total(clients)`: Displays the total balance and the total number of clients.
- `make_transfer(clients, sender_id, receiver_id, amount)`: Transfers a specified amount of money between two clients.
- `make_vip(clients, id)`: Makes a client a VIP if their balance exceeds 10,000 euros.
### `banking_2.py`
This file contains the main program that interacts with the user through a command-line interface. It provides a menu with options to perform different operations on the client data. The user can choose an option by entering the corresponding number. The available options include adding new clients, updating client information, deleting clients, displaying client details, displaying total balance and number of clients, making transfers, and making clients VIP.
## Getting Started
To run the **Banking project**, follow these steps:
1. Make sure you have Python installed on your system.
2. Download the `clients.json`, `banking_1.py`, and `banking_2.py` files.
3. Open a terminal or command prompt and navigate to the directory where the files are located.
4. Run the following command to start the program:
5. Follow the instructions in the command-line interface to interact with the program.
Note: Any changes made to the client data will be saved automatically to the `clients.json` file.
Feel free to explore the functionalities of the **Banking project** and manage client information efficiently!
*Note: This project is for demonstration purposes only and does not involve real banking operations. Use it responsibly and do not share sensitive information.*
Enjoy your banking experience!
