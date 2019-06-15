import socket
serverSocket = socket.socket()
port = 12345
print("Host Name: ", socket.gethostname())
serverSocket.bind((socket.gethostname(), port))
# No of users 1
serverSocket.listen(1)
conn, client_address = serverSocket.accept()
print("Connected To: ", client_address)
while True:
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            break
        print("Client: " + str(data))
        data = input(">> ")
        conn.send(data.encode())
conn.close()
