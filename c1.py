import socket

c = socket.socket()

c.connect(('localhost',9999))
# i want to send name to the server
name = input("Enter Your Name: ")
c.send(bytes(name,'utf-8'))

print(c.recv(1024).decode())
