# test
# 소켓 프로그래밍
# 서버 프로그램

#%%
from socket import *

host = '192.168.71.58'
port = 9999

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

server_socket.bind((host, port))
print("Listening....")

server_socket.listen()
client_socket, addr = server_socket.accept()
print("Connect by", addr)

while True:
    data = client_socket.recv(1024)
    if not data:
        break
    print("Received from :", addr, data.decode())
    client_socket.sendall(data + "~ , 나 Server 야 ~ 메세지 받았음 !!".encode())

client_socket.close()
server_socket.close()




#%%

