import socket

# tcp_server.py
# This script implements a simple TCP server for benchmarking latency.
# The server listens for incoming connections, receives data, and sends responses.

try:
    # create the server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    # bind the server to a specific address and port
    server_socket.bind(('localhost', 65432)) # Host on localhost and port 65432

    # listen for incoming connections
    server_socket.listen(1)
    print("Server is waiting for a connection...")

    # accept incoming connections
    conn, addr = server_socket.accept()
    print(f"Connected byt {addr}")

    # keep the server running and waiting for data
    while True:
        data = conn.recv(4096) # receive data from the client
        if not data:
            break  # exit the loop if no data is received
        print(f"Received: {len(data)} bytes from the client")
        conn.sendall(data)  # echo the received data back to the client

except Exception as e:
    print(f"Error: {e}")

finally:
    
    # close the connection
    conn.close()
