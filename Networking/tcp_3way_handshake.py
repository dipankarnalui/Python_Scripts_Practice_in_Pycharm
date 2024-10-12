#SYN: Client sends a SYN request to start a connection.
#SYN-ACK: Server responds with a SYN-ACK to acknowledge and synchronize.
#ACK: Client sends an ACK to confirm, establishing the connection.

import socket
import time

# Simulating a server that performs a 3-way handshake
def tcp_server(host='127.0.0.1', port=65432):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("Server listening on port", port)

    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    # Step 2: Receive SYN from client
    data = conn.recv(1024)
    if data == b'SYN':
        print("Received SYN from client.")
        
        # Step 2: Send SYN-ACK to client
        conn.send(b'SYN-ACK')
        print("Sent SYN-ACK to client.")
        
        # Step 3: Receive ACK from client
        data = conn.recv(1024)
        if data == b'ACK':
            print("Received ACK from client. Connection established.")

    conn.close()
    server_socket.close()

# Simulating a client that performs a 3-way handshake
def tcp_client(host='127.0.0.1', port=65432):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print("Client connected to server.")

    # Step 1: Send SYN to server
    client_socket.send(b'SYN')
    print("Sent SYN to server.")
    
    # Step 2: Receive SYN-ACK from server
    data = client_socket.recv(1024)
    if data == b'SYN-ACK':
        print("Received SYN-ACK from server.")
        
        # Step 3: Send ACK to server
        client_socket.send(b'ACK')
        print("Sent ACK to server. Connection established.")

    client_socket.close()

# Example usage
if __name__ == '__main__':
    import threading
    
    # Run server and client in different threads to simulate interaction
    server_thread = threading.Thread(target=tcp_server)
    client_thread = threading.Thread(target=tcp_client)

    server_thread.start()
    time.sleep(1)  # Ensure server starts before client
    client_thread.start()

    server_thread.join()
    client_thread.join()
