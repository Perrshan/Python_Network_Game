# Overview

I am expanding my coding knowledge and decided to learn more about how to set up servers and clients to play games across computers. I designed a simple game where two users repeatedly send words in trying to send the same word.

[Software Demo Video](https://youtu.be/4fSW06mvPuA)

# Network Communication

The architecture that I used was Server to Client meaning that one or more clients can connect to a server to receive data. I am using TCP for this program and the port number I am using is `12345`. For the messages sent I was using the `client_socket.sendall()` function along with the `encode()` function to convert it to binary. To receive messages I was using the `client_socket.recv(<accepted length>)` function which along with the `decode()` function to convert it back to the original text.

# Development Environment

* Visual Studio Code
* Windows Command Terminal
* Python
* TCP
* socket
* threading

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Client to Server Model](https://en.wikipedia.org/wiki/Client%E2%80%93server_model)
* [Difference between TCP and UDP](https://www.howtogeek.com/190014/htg-explains-what-is-the-difference-between-tcp-and-udp/)
* [TCP Server Example](https://pymotw.com/2/socket/tcp.html)

# Future Work

* Clean up code and add more descriptive comments
* Make sure that server knows when everyone has left the game and to close
* Make more game functionalities to make the game more exciting. Like update the clients with more information as the game is going on or keep track of how many times it takes them to find a match