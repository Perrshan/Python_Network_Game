import socket
import threading

# Global variable to track game status
game_started = False
first_client = True
client_words = []

# Event to synchronize word entry for both clients
word_entry_event = threading.Event()

# Function to listen for incoming connections
def accept_clients(server_socket):
    while True:
        # Wait for a connection
        print('Waiting for a connection...')
        client_socket, client_address = server_socket.accept()

        # Start a new thread to handle the connection
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

def handle_client(client_socket, client_address):
    global game_started
    global first_client

    # Receive username from the client
    username = client_socket.recv(1024).decode()
    print(f'Player {username} has joined the game')

    if first_client:
        first_client = False
        client_socket.sendall('1'.encode())
        start_signal = client_socket.recv(1024).decode()
        if start_signal.strip().lower() == 'start':
            game_started = True
            print('Game started!')
    else:
        client_socket.sendall('0'.encode())
        while not game_started:
            True
    game(client_socket, username)

def game(client_socket, username):
    # Game loop
    global client_words

    game_over = False
    while not game_over:
        # Wait for the client to enter a word
        if len(client_words) == 0:
            client_socket.sendall('start'.encode())

        word = client_socket.recv(1024).decode()
        
        # Store the username and word in the client_words dictionary
        client_words.append(word)

        print(client_words)
        print(len(client_words))

        # Wait for both clients to enter a word
        while len(client_words) % 2 != 0:
            pass

        # Notify both clients that both words have been received
        client_socket.sendall(str('Previous Guesses: '+ client_words[-1] + ', ' +client_words[-2]).encode())

        if client_words[-1].lower() == client_words[-2].lower():
            game_over = True
            client_socket.sendall('solved'.encode())
            break
        else:
            client_socket.sendall('continue'.encode())

    # Clean up the connection outside the loop
    print(f'Player {username} has left the game')
    client_socket.close()

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the IP address and port on which the server will listen
server_address = ('localhost', 12345)

# Bind the socket to the server address
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(2)

print('Server is listening on {}:{}'.format(*server_address))

# Start a thread to accept incoming connections
accept_thread = threading.Thread(target=accept_clients, args=(server_socket,))
accept_thread.start()

# Wait for the accept thread to finish
accept_thread.join()
    
server_socket.close()