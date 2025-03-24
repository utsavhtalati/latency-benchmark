import socket
import time

# tcp_client.py
# This script implements a simple TCP client for benchmarking latency.
# It connects to a TCP server, sends a message, and measures the round-trip time.

try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to the server at localhost on port 65432
    client_socket.connect(('localhost', 65432))

    # List of message sizes in bytes 
    # 4KB, 8KB, 16KB, 32KB, 64KB, 1MB, 5MB (TBD)
    message_sizes = [4096, 8192, 16384, 32768, 65536, 1048576]

    # loop through each message size and send the message

    for size in message_sizes:
        message = "A" * size

        # measure RTT (round-trip time)
        start_time = time.perf_counter()

        client_socket.sendall(message.encode())

        # receive the response from the server
        data = client_socket.recv(1024)
        end_time = time.perf_counter()

        print(f"Sent {size} bytes, received: {data.decode()}")

        # calculate and print the RTT
        rtt = end_time - start_time
        print(f"RTT: for {size} bytes: {rtt:.6f} seconds\n")


except Exception as e:
    print(f"Error: {e}")

finally:
    # close the connection
    client_socket.close()