import socket
import datetime

# Server configuration
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 9999

# Connect to server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_PORT))

print("   \   / /--\ |  |   | YOU ARE NOW BEING CONNECTED TO THE SERVER")
print("    \ /  |  | |  |   | SERVER = ('127.0.0.1',9999)")
print("     |   |  | |  |   | ")
print("     |   \--/ \--/   | v=0.0.0.1 Beta")

print("")
print(f"[!] CONNECTED TO SERVER BASELINE AT {datetime.datetime.now()}")

client_socket.send("SERVER MANAGER, LOL!!!".encode())
response = client_socket.recv(1024)

# Send commands until user types "exit"
while True:
    command = input("> ")
    if command.lower() == "exit":
        break
    if command.lower() == "":
        continue
    if command.lower() == "nodes":
        client_socket.send("nodes".encode())
        response = client_socket.recv(1024).decode()
        print("Connected Nodes:")
        print(response)
        continue

    if command.lower() == "close*":
        client_socket.send("T76r6t66r^&7v76R6r76VR876vr86R65vr6%RV%^vr56R56vr67VR6e^5EV&6E6e67676R5D65f6F65fV6%fv65F^f^tF6tf*76VVF6VR865vr65R86vr65".encode())
        print("Closing all connections...")
        break

    if command.lower().startswith("node -disconnect"):
        try:
            # Extract IP address and port from the command
            ip_port = command.split()[2]
            ip, port = ip_port.strip('()').split(',')
            ip = ip.strip("'")
            port = int(port.strip("'"))
            print(f"Disconnecting node at {ip}:{port}")
            # Send "CLOSE*con" command to disconnect the specified node
            client_socket.send(f"CLOSE*con {ip}:{port}".encode())
        except Exception as e:
            print("Invalid command format. Use 'node -disconnect $ipaddresswithport'")
            print("Example: node -disconnect ('127.0.0.1',55094)")
        continue

    client_socket.send(command.encode())

    # Receive response from server
    response = client_socket.recv(1024)
    print("", response.decode())

client_socket.close()
