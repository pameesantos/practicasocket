import sys
import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5664
BUFFER_SIZE = 20

print ("[CLIENTE] Iniciando")

mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print ("[CLIENTE] Conectando")
mi_socket.connect((TCP_IP, TCP_PORT))
print ("[CLIENTE] soy el cliente: \"" + str(mi_socket.getsockname) + "\"")
#print ("[CLIENTE] Enviando datos: \"" + MESSAGE + "\"")
MESSAGE = ''
while MESSAGE != "SALIR":
	MESSAGE = input('Ingrese dato: ')
	mi_socket.send((MESSAGE + '\n').encode('utf-8'))
	
	
print ("[CLIENTE] Recibiendo datos del CLIENTE")

msg = ''
fin_msg = False
datos = bytearray()
while not fin_msg:
	recibido = mi_socket.recv(BUFFER_SIZE)
	datos += recibido
	#print ("[CLIENTE] Recibidos ", len(recvd), " bytes")
	if b'\n' in recvd:
		msg = datos.rstrip(b'\n').decode('utf-8')
		fin_msg = True
#print ("[CLIENTE] Recibidos en total ", len(datos), " bytes")
#print ("[CLIENTE] Dados recibidos en respuesta al CLIENTE: \"" + msg + "\"")
print ("[CLIENTE] Cerrando conexion con el CLIENTE")
mi_socket.close()

print ("[CLIENTE] Fin")