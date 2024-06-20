import threading
import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5664
BUFFER_SIZE = 20 
cant_cli = 0
lista_conexiones = []
   
def atiende_cliente(conn, addr):
    try: #Se utiliza para poder atrapar los errores que puedan llegar a surgir cuando se corra el código que está dentro del try, en este caso, pretendo atrapar errores que pueden surgir al recibir datos del cliente
        msg = ''
        datos = bytearray()
        while 1:
            recvd = conn.recv(BUFFER_SIZE) #Se recibe el mensaje del cliente
            if not recvd:
                raise ConnectionError()
                break
            datos= recvd
            if b'\n' in recvd:
                msg = datos.rstrip(b'\n').decode('utf-8')            
            print ("Cliente: ", msg )
            if msg[0] == '#':
                reenviar(msg) #se llama a la función que verifica si se reenvia o no el mensaje enviado por el cliente
            elif msg.upper() == 'LOGOUT': #Aca se determina si se cierra o no la conexión
                conn.close()
                break
            elif msg == '?': #Cuando el cliente digite ? debe mostrar las opciones que tiene para salir y para reenviar el mensaje
                menu='\n'+" -   Ingrese # al principio del mensaje para reenviarlo a todos" + '\n' + "Ingrese LOGOUT para finalizar conexión"
                conn.send((menu + '\n').encode('utf-8'))  
            else:
                msje_serv=responde_cliente(conn,addr) #Se pide respuesta para el cliente
                conn.send((msje_serv + '\n').encode('utf-8')) #En caso de que no se cierre, se envia el mensaje que se pidió en la línea 25
    except BaseException as error: #Se detecta errores de conexión con el cliente y muestra el mensaje de error devuelto
        print ("[SERVIDOR ", addr, "] [ERROR] Socket error: ", error)

    print ("[SERVIDOR ", addr, "] cerrando conexion ", addr)
    conn.close()

def responde_cliente(conn,addr): #Se ingresa el mensaje que se le va enviar al cliente
    msje = input()
    return msje


def finalizachat(msje_serv,msje_cli,conn): # Se verifica si se cierra o no la conexión (condición: recibir LOGOUT de ambas partes)
    if msje_cli == 'LOGOUT' and msje_serv == 'LOGOUT':
        conn.close()
        return 1
    return 0
def reenviar(msje_cli): #Se reenvia el mensaje a todos los clientes
    for cliente in lista_conexiones:
        cliente.send((msje_cli + '\n').encode('utf-8'))

##################################### PROGRAMA PRINCIPAL #############################################
print ("[SERVIDOR] Iniciando")
print ("[SERVIDOR] Abriendo socket " + str(TCP_PORT) + " y escuchando")
mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mi_socket.bind((TCP_IP, TCP_PORT))
mi_socket.listen(1)

while 1:
    print ("[SERVIDOR] Esperando conexion")
    conn, addr = mi_socket.accept()
    lista_conexiones.append(conn) #Se hace una lista llenandose de las conexiones que se van aceptando
    thread = threading.Thread(target=atiende_cliente, 
                              args=[conn, addr],
                              daemon=True)
    #Se abre un hilo por cada conexión activa
    thread.start()
    cant_cli +=1 #es un contador de clientes conectados que en la siguiente linea se imprime
    print ('Cliente N°:', cant_cli)
    print ("[SERVIDOR ", addr, "] Conexion con el cliente realizada. Direccion de conexion:", addr)

print ("[SERVIDOR] Cerrando socket " + str(TCP_PORT))
mi_socket.close()

print ("[SERVIDOR] fin_msg")


