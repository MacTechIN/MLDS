# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 14:56:42 2023

@author: Solero
"""

# client socket

from socket import *

host = "127.0.0.1"
port = 9999

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((host, port))
client_socket.sendall("안녕".encode())

data = client_socket.recv(1024)

print("Received from:", repr(data.decode()))

client_socket.close()