import socket

s = socket.socket()
# print(s)
# print(type(s))
print("Socket Created")

s.bind(("localhost",9999))

s.listen(0)
print("Waiting for connection")

while True:
    c,addr = s.accept()
    name = c.recv(1024).decode()
    print("Connected With ", addr,name)
    # before sending data to client , we should recive
    # data from client
   
    c.send(bytes("Welcome","utf-8"))
    c.close() 
    

