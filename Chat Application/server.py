from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
import tkinter
import rsa

public_key, private_key = rsa.newkeys(512)


class Connection:

    def __init__(self, conn, addr):
        self.conn = conn
        self.addr = addr
        self.name = 'N/A'

class Server:
    def __init__(self):
        host = '127.0.0.1'
        port = 21568
        self.buffer_size = 1024
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.clients = {}
        self.users = []
        self.server_socket.listen()
        self.window = tkinter.Tk()
        self.add_online_user_box()
        self.start()


    def start(self):
        main_thread = Thread(target=self.accept_connections)
        main_thread.start()
        main_thread.join()
        self.server_socket.close()

    def add_online_user_box(self):
        self.lbl = tkinter.Label(self.window, text="Online Users")
        self.listbox = tkinter.Listbox(self.window)
        self.lbl.pack()
        self.listbox.pack()

    def accept_connections(self):
        while True:
            print('waiting for connection...')
            conn, addr = self.server_socket.accept()
            print('...connected from:', addr)
            self.clients[conn] = Connection(conn, addr)

            #Get client's public key
            pk = conn.recv(1024)
            self.client_key = rsa.PublicKey.load_pkcs1(pk)

            #Send server key
            pk_bytes = public_key.save_pkcs1()
            conn.send(pk_bytes)

            th = Thread(target=self.client_thread, args=(conn,))
            th.start()

    def client_thread(self, client):
        message = "Welcome, please type your name"
        message_bytes = bytes(message, "utf8")
        encrypted_message = self.encrypt_message(message_bytes)
        client.send(encrypted_message)

        name = client.recv(self.buffer_size)
        nam = self.decrypt_message(name)
        client.send(bytes("Hi " + nam + ", type close when you want to leave.", "utf8"))
        # broadcast name
        self.clients[client].name = nam
        message = bytes(nam, "utf8") + bytes(" has joined the chat.", "utf8")
        enc_message = self.encrypt_message(message)
        self.join_chat(enc_message, nam)

        while True:
            enc_msg = client.recv(self.buffer_size)
            decoded_msg = self.decrypt_message(enc_msg)

            if decoded_msg == bytes("close", "utf8"):
                del self.clients[client]
                message = bytes(name, "utf8") + bytes(" leaving chat", "utf8")
                encrypted_message = self.encrypt_message(message)
                self.broadcast(encrypted_message)
                break
            else:
                message = bytes(name, "utf8") + bytes(": ", "utf8") + bytes(decoded_msg, "utf8")
                encrypted_message = self.encrypt_message(message)
                self.broadcast(encrypted_message)

    def broadcast(self, msg):
        for client in self.clients:
            client.send(msg)

    def join_chat(self, msg, name):
        for client in self.clients:
            if name != self.clients[client].name:
                client.send(msg)

    def encrypt_message(self, msg):
        enc_msg = rsa.encrypt(msg, self.client_key)
        return enc_msg

    def decrypt_message(self, msg):
        dec_msg = rsa.decrypt(msg, private_key)
        decoded_msg = dec_msg.decode('utf8')
        return decoded_msg

if __name__ == '__main__':
    server = Server()
