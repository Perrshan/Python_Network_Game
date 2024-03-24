import socket

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
server_address = ('localhost', 12345)
client_socket.connect(server_address)

try:
    # Send username to the server
    username = input("Enter a username: ")
    client_socket.sendall(username.encode())

    host = int(client_socket.recv(1024).decode())  # Convert to integer

    # If the client is the host, prompt for game start
    if host == 1:
        while True:
            start = input('You are the host! Enter "start" when everyone is ready to go! ')
            if start == "start":
                client_socket.sendall("start".encode())
                break
    else:
        print("Welcome! Please wait for the host to begin the game.")

        # Modify the loop to wait for the signal from the server

    while True:
        game_status = client_socket.recv(1024).decode()

        if game_status == 'start':
            print('The Game has started! Continue to enter and try to match the word of your partner. The best way to win is to try to choose a word in between the two words that were entered previously!')

        if game_status == 'solved':
            print('You win!')
            break
        
        word = input('Enter a word trying to match the word of your teammate: ')
        client_socket.sendall(word.encode())
        
        print("Please wait until your teammate sends their word! ")

        words = client_socket.recv(1024).decode()
        print(words)

finally:
    # Clean up the connection
    client_socket.close()