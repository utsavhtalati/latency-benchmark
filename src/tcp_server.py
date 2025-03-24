import socket
import threading

# tcp_server.py
# This script implements a simple TCP server for benchmarking latency.
# The server listens for incoming connections, receives data, and sends responses.

def handle_client(conn, addr):
    print(f"New connection from {addr}")
    while True:
        data = conn.recv(4096)  # receive data from the client
        if not data:
            break
        print(f"Received: {len(data)} bytes from {addr}")
        conn.sendall(data) # echo the received data back to the client
    print(f"Connection closed: {addr}")
    conn.close()

try:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind and listen for connection
    server_socket.bind(('localhost', 65432))
    server_socket.listen(5)
    print("Server waiting for connections...")

    while True:
        conn, addr = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()

except Exception as e:
    print(f"Error: {e}")

finally:
    server_socket.close()
