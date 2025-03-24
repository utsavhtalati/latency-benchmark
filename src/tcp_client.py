import socket
import time

# tcp_client.py
# This script implements a simple TCP client for benchmarking latency.
# It connects to a TCP server, sends a message, and measures the round-trip time.

try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to the server at localhost on port 65432
    client_socket.connect(('localhost', 65432))

    # message to be sent to the server
    message = "Hello, Server!"

    # Measure the round-trip time (RTT)
    start_time = time.perf_counter()
    client_socket.sendall(message.encode())  # send the message to the server

    # receive the echoed message from the server
    data = client_socket.recv(1024)  # buffer size of 1024 bytes
    end_time = time.perf_counter()

    print(f"Received from server: {data.decode()}")
except Exception as e:
    print(f"Error: {e}")

finally:
    # close the connection
    client_socket.close()