# practicasocket
Socket: Servidor concurrente

Se debe ejecutar primero el archivo server.py y luego el archivo client.py tantas veces como clientes se quiere conectar al servidor.

Para finalizar la conexión desde el cliente se debe mandar LOGOUT y el servidor debe responder también LOGOUT

Para que el mensaje enviado por el cliente sea reenviado a todos los clientes, se le debe poner al mensaje un # al principio del mismo, de esta manera el servidor recibe el mensaje y lo reenvía a todos los clientes conectados

El puerto utilizado fue designado por el profesor: 5664 