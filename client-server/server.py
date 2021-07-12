import socket

mi_socket = socket.socket()
mi_socket.bind (('localhost', 5555))
mi_socket.listen(5)

while True:
    conexion, addr = mi_socket.accept()
    print "Conexion Establecita!"
    print addr

    conexion.send("hola habla el servidor")
    conexion.close()