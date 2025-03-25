import socket
import threading

# Handles a client connection
def handle_client(conn, addr):
    print(f"New connection from {addr}")
    try:
        while True:
            # Read the message length (8-byte header)
            length_data = conn.recv(8)
            if not length_data:
                break

            # Get the expected message length
            message_length = int.from_bytes(length_data, byteorder='big')
            print(f"Expecting {message_length} bytes from {addr}")

            # Read the message in chunks
            data = b""
            while len(data) < message_length:
                chunk = conn.recv(min(4096, message_length - len(data)))
                if not chunk:
                    raise ConnectionError("Client disconnected before sending all data.")
                data += chunk

            print(f"Received: {len(data)} bytes from {addr}")

            # Send acknowledgment
            conn.sendall(b"ACK")

    except Exception as e:
        print(f"Error handling client {addr}: {e}")

    finally:
        print(f"Connection closed: {addr}")
        conn.close()

# Main server setup
try:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind and listen on localhost:65432
    server_socket.bind(('localhost', 65432))
    server_socket.listen(5)
    print("Server waiting for connections...")

    while True:
        conn, addr = server_socket.accept()
        threading.Thread(target=handle_client, args=(conn, addr)).start()

except Exception as e:
    print(f"Server Error: {e}")

finally:
    server_socket.close()
