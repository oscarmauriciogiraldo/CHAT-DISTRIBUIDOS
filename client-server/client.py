import socket 

mi_socket = socket.socket()
mi_socket.connect (('localhost', 5555))

mi_socket.send("hola mk soy el cliente entienda")
respuesta = mi_socket.recv(1024)

print respuesta