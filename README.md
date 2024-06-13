# practicasocket
Socket: Servidor concurrente
Este programa permite una comunicación entre servidor y clientes, simulando un chat.

Se debe ejecutar primero el archivo server.py y luego el archivo client.py tantas veces como clientes se quiere conectar al servidor.

Para finalizar la conexión el cliente debe mandar LOGOUT

Para que el mensaje enviado por el cliente sea reenviado a todos los clientes, se le debe poner al mensaje un # al principio del mismo, de esta manera el servidor recibe el mensaje y lo reenvía a todos los clientes conectados

El puerto utilizado fue designado por el profesor: 5664 