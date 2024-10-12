#1. Host A → Host B: FIN flag set.
#2. Host B → Host A: ACK flag set.
#3. Host B → Host A: FIN flag set.
#4. Host A → Host B: ACK flag set.


import socket
import time

# Simulating a server that accepts a connection and performs the 4-way handshake
def tcp_server(host='127.0.0.1', port=65432):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("SERVER:: Server listening on port", port)
    
    conn, addr = server_socket.accept()
    print(f"SERVER:: Connected by {addr}")

    # Simulating receipt of the FIN from the client
    data = conn.recv(1024)
    if data == b'FIN':
        print("SERVER:: Received FIN from client.")
        # Send ACK for client's FIN
        conn.send(b'ACK')
        time.sleep(1)  # Simulate processing delay
        
        # Send FIN from the server
        conn.send(b'FIN')
        print("SERVER:: Sent FIN to client.")
        
        # Receive ACK for server's FIN
        data = conn.recv(1024)
        if data == b'ACK':
            print("SERVER:: Received ACK from client. Connection terminated.")
    
    conn.close()
    server_socket.close()

# Simulating a client that connects to a server and performs the 4-way handshake
def tcp_client(host='127.0.0.1', port=65432):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print("CLIENT:: Client connected to server.")

    # Send FIN from the client
    client_socket.send(b'FIN')
    print("CLIENT:: Sent FIN to server.")
    
    # Receive ACK for client's FIN
    data = client_socket.recv(1024)
    if data == b'ACK':
        print("CLIENT:: Received ACK from server.")
    
    # Receive FIN from server
    data = client_socket.recv(1024)
    if data == b'FIN':
        print("CLIENT:: Received FIN from server.")
        # Send ACK for server's FIN
        client_socket.send(b'ACK')
        print("CLIENT:: Sent ACK to server. Connection terminated.")
    
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
