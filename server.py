import threading
import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5664
BUFFER_SIZE = 20 
#mi_socket = socket.socket()
def atiende_cliente(conn, addr):
    while 1:
        msg = ''
        datos = bytearray()
        print ("[SERVIDOR ", addr, "] Esperando datos del cliente")
        fin_msg = False
        try:
            while not fin_msg:
                recvd = conn.recv(BUFFER_SIZE)
                if not recvd:
                    raise ConnectionError()
                    break
                datos += recvd
                print ("[SERVIDOR ", addr, "] Recibidos ", len(recvd), " bytes")
                if b'\n' in recvd:
                    msg = datos.rstrip(b'\n').decode('utf-8')            
                    fin_msg = True
            #print ("[SERVIDOR ", addr, "] Recibidos en total ", len(datos), " bytes")
            print ("[SERVIDOR ", addr, "] Datos recibidos del cliente con exito: \"" + msg + "\"")
            #print ("[SERVIDOR ", addr, "] Enviando respuesta para el cliente")
            conn.send(datos)  # echo
            #print ("[SERVIDOR ", addr, "] Respuesta enviada: \"" + msg + "\"")
            #conn.close()
        except BaseException as error:
            print ("[SERVIDOR ", addr, "] [ERROR] Socket error: ", error)
            break
    print ("[SERVIDOR ", addr, "] cerrando conexion ", addr)
    conn.close()


print ("[SERVIDOR] Iniciando")

print ("[SERVIDOR] Abriendo socket " + str(TCP_PORT) + " y escuchando")
mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mi_socket.bind((TCP_IP, TCP_PORT))
mi_socket.listen(1)

while 1:
    print ("[SERVIDOR] Esperando conexion")
    conn, addr = mi_socket.accept()
    thread = threading.Thread(target=atiende_cliente,
                              args=[conn, addr],
                              daemon=True)
    thread.start()
    print ("[SERVIDOR ", addr, "] Conexion con el cliente realizada. Direccion de conexion:", addr)    

print ("[SERVIDOR] Cerrando socket " + str(TCP_PORT))
mi_socket.close()

print ("[SERVIDOR] fin_msg")

