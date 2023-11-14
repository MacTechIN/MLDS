


from socket import *

host = '192.168.71.200'
port = 9999

client_socket = socket(AF_INET,SOCK_STREAM)
client_socket.connect(((host,port)))
client_socket.sendall("안녕! 전 이상진입니다~ ".encode())

data = client_socket.recv(1024)
data = data + ",OK!".encode()

print("Received from :",host ,":" , repr(data.decode()))

client_socket.close()
