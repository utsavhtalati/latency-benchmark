import socket
import time

# Send a message with a length header
def send_with_header(sock, message):
    message = message.encode()  # Ensure message is bytes
    message_length = len(message)

    # Send the length header (8 bytes) and the message
    sock.sendall(message_length.to_bytes(8, 'big'))
    sock.sendall(message)

# Client 
try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server at localhost on port 65432
    client_socket.connect(('localhost', 65432))

    # List of message sizes in bytes
    message_sizes = [4096, 8192, 16384, 32768, 65536, 1048576, 5242880]

    # Loop through each message size and measure latency
    for size in message_sizes:
        message = "A" * size

        # Measure round-trip time (RTT)
        start_time = time.perf_counter()

        send_with_header(client_socket, message)

        # Wait for acknowledgment from the server
        data = client_socket.recv(1024)
        end_time = time.perf_counter()

        print(f"Sent {size} bytes, received: {data.decode()}")

        # Calculate and print the RTT
        rtt = end_time - start_time
        print(f"RTT for {size} bytes: {rtt:.6f} seconds\n")

except Exception as e:
    print(f"Client Error: {e}")

finally:
    client_socket.close()
