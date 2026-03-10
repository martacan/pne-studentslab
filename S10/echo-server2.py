import socket

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Configure the Server's IP and PORT
PORT = 8080
IP = "212.128.255.80"

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()
connection_count = 0
print(f"The server is configured on port {PORT}")

while True:

    print("Waiting for Clients to connect")
    (cs, client_ip_port) = ls.accept()
    connection_count += 1

    client_ip = client_ip_port[0]
    client_port = client_ip_port[1]

    print(f" Connection:{connection_count} from {client_ip} port {client_port}")


    msg_raw = cs.recv(2048)
    msg = msg_raw.decode()

    print(f"Message received: {msg}")

    # -- Send a response message to the client
    response = "ECHO: " + msg

    # -- The message has to be encoded into bytes
    cs.send(response.encode())

    # -- Close the data socket
    cs.close()