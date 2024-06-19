import socket

def main():
    # Define the host and port to listen on
    host = "0.0.0.0"  # Listen on all available interfaces
    port = 443

    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Bind the socket to the host and port
        server_socket.bind((host, port))

        # Listen for incoming connections
        server_socket.listen(5)

        print(f"Server listening on {host}:{port}")

        while True:
            # Accept incoming connection
            client_socket, client_address = server_socket.accept()
            print(f"Connection from {client_address}")

            # Handle the connection (you can add your custom logic here)
            # For example, you can receive data from the client
            data = client_socket.recv(1024)
            if data:
                print(f"Received data from client: {data.decode('utf-8')}")

            # Close the client socket
            client_socket.close()

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the server socket
        server_socket.close()

if __name__ == "__main__":
    main()
