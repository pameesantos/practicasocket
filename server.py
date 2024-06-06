import threading
import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5664
BUFFER_SIZE = 20 
cant_cli = 0
lista_conexiones = []
def atiende_cliente(conn, addr):
    while 1:
        msg = ''
        datos = bytearray()
        fin_msg = False
        try:
            while 1:
                recvd = conn.recv(BUFFER_SIZE) #Se recibe el mensaje del cliente
                if not recvd:
                    raise ConnectionError()
                    break
                datos += recvd
                if b'\n' in recvd:
                    msg = datos.rstrip(b'\n').decode('utf-8')            
                print ("Cliente: ", msg )
                reenviar(msg,conn,addr) #se llama a la función que verifica si se reenvia o no el mensaje enviado por el cliente
                msje_serv=responde_cliente(conn,addr) #Se pide respuesta para el cliente
                if (msje_serv.upper() == 'LOGOUT' and msg.upper() == 'LOGOUT'): #Aca se determina si se cierra o no la conexión
                    break
                conn.send((msje_serv + '\n').encode('utf-8')) #En caso de que no se cierre, se envia el mensaje que se pidió en la línea 25

        except BaseException as error:
            print ("[SERVIDOR ", addr, "] [ERROR] Socket error: ", error)
            break
    print ("[SERVIDOR ", addr, "] cerrando conexion ", addr)
    conn.close()

def responde_cliente(conn,addr): #Se ingresa el mensaje que se le va enviar al cliente
    msje = input('Servidor: ')
    return msje


def finalizachat(msje_serv,msje_cli,conn): # Se verifica si se cierra o no la conexión (condición: recibir LOGOUT de ambas partes)
    if msje_cli == 'LOGOUT' and msje_serv == 'LOGOUT':
        conn.close()
        return 1
    return 0
def reenviar(msje_cli,conn,addr): #Se verifica si el mensaje recibido por el cliente tiene un # al principio
    if '#' in msje_cli:  #En caso de que si, se envía ese mensaje a todos los clientes conectados
        for cliente in lista_conexiones:
            cliente.sendall((msje_cli + '\n').encode('utf-8'))


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


