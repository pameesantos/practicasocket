import sys
import socket

def escucha_servidor(): #Acá se escucha si el servidor envía un mensaje y lo imprime
    try:
        datos = mi_socket.recv(1024)
        if b'\n' in datos:
            msg = datos.rstrip(b'\n').decode('utf-8')            
        print('Servidor: ',datos.decode())
    except:
        print("Conexión cerrada por el servidor")
    return msg

TCP_IP = '127.0.0.1'
TCP_PORT = 5664
BUFFER_SIZE = 20

print ("[CLIENTE] Iniciando")

mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print ("[CLIENTE] Conectando")
mi_socket.connect((TCP_IP, TCP_PORT))


MESSAGE = ''
while 1:
    MESSAGE = input('Cliente: ') # se pide que ingrese a mano el usuario el mensaje que desee enviar
    mi_socket.send((MESSAGE + '\n').encode('utf-8')) #se envía el mensaje anterior
    if (MESSAGE.upper() == "LOGOUT"): #Acá se termina la conexión siempre y cuando se envie LOGOUT 
        mi_socket.close()    
        break
    msje_serv = escucha_servidor() #queda escuchando al servidor para recibir la respuesta        
	
	
print ("[CLIENTE] Recibiendo datos del CLIENTE")

print ("[CLIENTE] Cerrando conexion con el CLIENTE")
mi_socket.close()

print ("[CLIENTE] Fin")