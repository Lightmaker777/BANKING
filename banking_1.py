import json
import datetime


# Function ro load clients from thr json file
def load_clients():
    # open file in read mode by default
    with open('clients.json') as file:
        # load JSON from file
        data = json.load(file)
    return data['clients']

# Function save clients to the json file


def save_clients(clients):
    # open file in write mode
    with open('clients.json', 'w') as file:
        # bump (write) the clients to the file
        json.dump({'clients': clients}, file, indent=4)

# Function to get the age of a client


def get_age(dob):
    # convert the dob from string to datetime object
    date_of_birth = datetime.datetime.strptime(dob, '%Y-%m-%d')
    # get current date and time
    today = datetime.datetime.today()
    # calculate the age
    age = today.year - date_of_birth.year
    return age

# Function to add a new client


def add_clients(clients, name, dob, balance):
    # get the current clients
    # clients = load_clients()
    id = clients[-1]["id"] + 1
    # add the new client
    clients.append({
        'id': id,
        'name': name,
        'dob': dob,
        'balance': balance
    })
    # save the clients list to the json file
    save_clients(clients)

# Function to update a client
# if the id is not valid add statement that prints 'customer does not exist' in functions like update,delete, and display
def update_clients(clients, id, name=None, dob=None, balance=None):
    # Flag to keep track if the client is found
    client_found = False
    # loop through the clients
    for client in clients:
        # select the client by id and update
        if client['id'] == id:
            client_found = True
            if name:
                client['name'] = name
            if dob:
                client['dob'] = dob
            if balance:
                client['balance'] = balance
            break
    if not client_found:
        # Client id validation
        print('Customer does not exist')
        print()
    else:
        print("Client updated successfully.")
        print()
    
    # save the clients list to the json file
    save_clients(clients)   


# Function to delete a client


def delete_clients(clients, id):
    # Flag to keep track if the client is found
    client_found = False

    # Loop through the clients
    for index, client in enumerate(clients):
        # Select the client by id and delete
        if client['id'] == id:
            client_found = True
            del clients[index]
            break

    if not client_found:
        # Client id validation
        print('Customer does not exist')
        print()
    else:
        print("Client deleted successfully.")
        print()
    # Save the clients list to the json file
    save_clients(clients)


# Function to display client
def display_clients(clients, id):
    # Flag to keep track if the client is found
    client_found = False

    # Loop through the clients
    for client in clients:
        # If the id matches, display the client details
        if client['id'] == id:
            client_found = True
            print('ID: ', client['id'])
            print('Name: ', client['name'])
            print('Date of Birth: ', client['dob'])
            print('Age: ', get_age(client['dob']))
            print('Balance: ', client['balance'])
            print()
            break

    if not client_found:
        # Client id validation
        print('Customer does not exist')        
        print()
    else:
        print("Client displayed successfully.")
        print()

# Function to display all clients
def display_total(clients):
    # display the total number of clients and total balance in the bank from the list of clients
    total_balance = sum([client['balance'] for client in clients])
    print('Total money in the bank: ', total_balance)
    total = len(clients)
    print('Total number of clients: ', total)
    print() 
   

# Function to transfer money between two clients, add and remove the balance from the sender and receiver


def make_transfer(clients, sender_id, receiver_id, amount):
    sender_found = False
    receiver_found = False

    # Loop through the clients
    for client in clients:
        # Update the balance for the sender
        if client['id'] == sender_id:
            sender_found = True
            client['balance'] -= amount

        # Update the balance for the receiver
        if client['id'] == receiver_id:
            receiver_found = True
            client['balance'] += amount

        # Break the loop if both sender and receiver are found
        if sender_found and receiver_found:
            break

    if not sender_found:
        print('Sender does not exist')
        print()

    if not receiver_found:
        print('Receiver does not exist')
        print()
    else:
        print("Transfer made successfully.")
        print()

    # Save the clients list to the json file
    save_clients(clients)
#function called make_vip that  adds a keyword VIP and set it to be true if the balance of client is higher than 10000 euros
def make_vip(clients, id):
    # Loop through the clients
    for client in clients:
        # Find the client by ID
        if client['id'] == id:
            # Check if the balance is higher than 10000 euros
            if client['balance'] > 10000:
                client['VIP'] = True
                print('Client', id, 'is now a VIP.')
            break
    else:
        print('Client', id, 'does not exist.')

    # Save the clients list to the json file
    save_clients(clients)
