import sys
import socket

def escucha_servidor():
    #while 1:
    try:
        datos = mi_socket.recv(1024)
 #       if not datos:
 #           break
        print('Servidor: ',datos.decode())
    except:
        print("Conexión cerrada por el servidor")
  #      break

TCP_IP = '127.0.0.1'
TCP_PORT = 5664
BUFFER_SIZE = 20

print ("[CLIENTE] Iniciando")

mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print ("[CLIENTE] Conectando")
mi_socket.connect((TCP_IP, TCP_PORT))


MESSAGE = ''
while 1:
    MESSAGE = input('Cliente: ')
    mi_socket.send((MESSAGE + '\n').encode('utf-8'))
    if MESSAGE == "LOGOUT":
        break
    escucha_servidor()
	
	
print ("[CLIENTE] Recibiendo datos del CLIENTE")

print ("[CLIENTE] Cerrando conexion con el CLIENTE")
mi_socket.close()

print ("[CLIENTE] Fin")