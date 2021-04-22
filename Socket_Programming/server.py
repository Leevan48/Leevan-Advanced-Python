from socket import *

HOST = '127.0.0.1'
PORT = 21567
ADDR = (HOST, PORT)

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(ADDR)
server_socket.listen()

print('waiting for 1st connection...')
conn_a, addr_a = server_socket.accept()
print('...connected from:', addr_a)
conn_a.send(b'Hi, start sending messages')

print('waiting for 2nd connection...')
conn_b, addr_b = server_socket.accept()
print('...connected from:', addr_b)
conn_b.send(b'Hi, wait to get messages')

while True:
    data_bytes = conn_a.recv(1024)
    if not data_bytes:
        break
    conn_b.send(data_bytes)
    data = data_bytes.decode('utf-8')
    if data == "Close":
        break

conn_a.send(b'Bye...')
conn_a.close()
conn_b.send(b'Bye...')
conn_b.close()
server_socket.close()
print("Server stopped ...")