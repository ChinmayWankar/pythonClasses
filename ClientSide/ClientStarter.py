import socket
clientSocket = socket.socket()
port = 12345
ipAddress = input("Enter ip address of server")
clientSocket.connect((ipAddress, port))
message = input(">> ")
while message.lower().strip() != 'bye':
    clientSocket.send(message.encode())
    data = clientSocket.recv(1024).decode()
    print('Server: ' + data)
    message = input(">> ")
clientSocket.close()
