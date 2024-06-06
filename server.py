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
                recvd = conn.recv(BUFFER_SIZE)
                if not recvd:
                    raise ConnectionError()
                    break
                datos += recvd
                if b'\n' in recvd:
                    msg = datos.rstrip(b'\n').decode('utf-8')            
                print ("Cliente: ", msg )
                reenviar(msg,conn,addr)
                msje_serv=responde_cliente(conn,addr)
                print('esto dice msg:',msg)
                print('esto dice msje_serv:',msje_serv)
                if (msje_serv.upper() == 'LOGOUT' and msg.upper() == 'LOGOUT'):
                    #conn.close()
                    break
                #finaliza=finalizachat(msje_serv,msg,conn) 
                #if finaliza == 1:
                #    break
                conn.send((msje_serv + '\n').encode('utf-8'))

        except BaseException as error:
            print ("[SERVIDOR ", addr, "] [ERROR] Socket error: ", error)
            break
    print ("[SERVIDOR ", addr, "] cerrando conexion ", addr)
    conn.close()

def responde_cliente(conn,addr):
    msje = input('Servidor: ')
    #conn.send((msje + '\n').encode('utf-8'))
    return msje


def finalizachat(msje_serv,msje_cli,conn):
    if msje_cli == 'LOGOUT' and msje_serv == 'LOGOUT':
        conn.close()
        return 1
    return 0
def reenviar(msje_cli,conn,addr):
    if msje_cli.startswith('#'):
        for cliente in lista_conexiones:
            if cliente != conn:
                try:
                    cliente.sendall(msje_cli)
                except:
                    cliente.close()
                    lista_conexiones.remove(cliente)

print ("[SERVIDOR] Iniciando")
print ("[SERVIDOR] Abriendo socket " + str(TCP_PORT) + " y escuchando")
mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mi_socket.bind((TCP_IP, TCP_PORT))
mi_socket.listen(1)

while 1:
    print ("[SERVIDOR] Esperando conexion")
    conn, addr = mi_socket.accept()
    lista_conexiones.append(conn)
    thread = threading.Thread(target=atiende_cliente,
                              args=[conn, addr],
                              daemon=True)
    
    thread.start()
    cant_cli +=1
    print ('Cliente N°:', cant_cli)
    print ("[SERVIDOR ", addr, "] Conexion con el cliente realizada. Direccion de conexion:", addr)
    print (threading.active_count())    

print ("[SERVIDOR] Cerrando socket " + str(TCP_PORT))
mi_socket.close()

print ("[SERVIDOR] fin_msg")


