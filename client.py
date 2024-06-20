import sys
import socket
import threading
def escucha_servidor(conn): #Acá se escucha si el servidor envía un mensaje y lo imprime
    while True:
        try: #Este try se utiliza para atrapar los errores que puedan surgir al recibir datos del servidor
            msg = conn.recv(1024)
            if not msg:
                break
            print('Servidor: ',msg.decode())
        except: #Este except va junto con el try, lo que hace que se muestre un mensaje mas amigable al usuario y no el error que devuelve realmente
            print("Conexión cerrada por el servidor")
            break
    
########################################### EMPIEZA EL PROGRAMA ############################################
TCP_IP = '127.0.0.1'
TCP_PORT = 5664
BUFFER_SIZE = 20
MESSAGE = ''

print ("[CLIENTE] Iniciando")

mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print ("[CLIENTE] Conectando")
mi_socket.connect((TCP_IP, TCP_PORT))

hilo_receptor = threading.Thread(target=escucha_servidor, args=(mi_socket,))
hilo_receptor.start() #En estas dos líneas se abre un hilo para que el cliente esté siempre escuchando lo que dice el servidor

try:
    while 1:
        MESSAGE = input()
        mi_socket.send((MESSAGE + '\n').encode('utf-8')) #se envía el mensaje anterior
        if (MESSAGE.upper() == "LOGOUT"): #Acá se termina la conexión siempre y cuando se envie LOGOUT   
            break
except BaseException as error:
    print ("Has finalizado la conexión")
	
print ("[CLIENTE] Cerrando conexion con el CLIENTE")

mi_socket.close()

print ("[CLIENTE] Fin")