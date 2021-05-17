from socket import socket, AF_INET, SOCK_STREAM
import tkinter
from threading import Thread
import rsa

public_key, private_key = rsa.newkeys(512)


class Client:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Python Skype Clone")
        self.add_message_list()
        self.add_message_field()
        self.connect()
        tkinter.mainloop()

    def add_message_list(self):
        frame = tkinter.Frame(self.window)
        scrollbar = tkinter.Scrollbar(frame)
        self.message_list = tkinter.Listbox(frame, height=15, width=50, yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.message_list.pack(side=tkinter.LEFT)
        frame.pack()


    def add_message_field(self):
        self.message_field = tkinter.Entry(self.window)
        self.message_field.pack()
        self.send_button = tkinter.Button(self.window, text="Send", command=self.send)
        self.send_button.pack()


    def connect(self):
        host = '127.0.0.1'
        port = 21568
        self.buffer_size = 1024
        self.client_socket = socket(AF_INET, SOCK_STREAM)
        self.client_socket.connect((host, port))

        # Send the public key of the client
        pk_bytes = public_key.save_pkcs1()
        self.client_socket.send(pk_bytes)

        # Read the server's public key
        pk = self.client_socket.recv(1024)
        self.server_key = rsa.PublicKey.load_pkcs1(pk)

        th = Thread(target=self.receive)
        th.start()

    def receive(self):
        while True:
            msg = self.client_socket.recv(self.buffer_size)
            dec_msg = self.decrypt_message(msg)
            self.message_list.insert(tkinter.END, dec_msg)


    def send(self):
        msg = self.message_field.get()
        message_bytes = msg.encode('utf8')
        message_enc = self.encrypt_message(message_bytes)
        self.message_field.delete(0, "end")
        self.client_socket.send(message_enc)
        if msg == "close":
            self.window.quit()

    def encrypt_message(self, msg):
        enc_msg = rsa.encrypt(msg, self.server_key)
        return enc_msg

    def decrypt_message(self, msg):
        dec_msg = rsa.decrypt(msg, private_key)
        decoded_msg = dec_msg.decode('utf8')
        return decoded_msg

if __name__ == '__main__':
    client = Client()