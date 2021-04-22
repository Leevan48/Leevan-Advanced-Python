from socket import *

HOST = '127.0.0.1'
PORT = 21567
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

data_bytes = client_socket.recv(1024)
data = data_bytes.decode('utf-8')
print(data)

while True:
    data = input('> ')
    data_bytes = str.encode(data)
    if not data:
        break
    client_socket.send(data_bytes)
    if data == "Close":
        break


client_socket.close()