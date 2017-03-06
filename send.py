import pika

# Estas dos lineas crean la conexion con el servidor rabbitMQ, en este caso
# el servidor esta instalado en esta maquina por eso apunta a localhost
# en caso de que este en una pc remota hay que escribir la ip.


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

# Se le da un nombre a la cola

channel.queue_declare(queue='hello')

# Se publica el mensaje especificando el nombre de la pila en el parametro routing_key
# el mensaje en el parametro body y exchange se vera mas adelante.

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hola World!')
print(" [x] Sent 'Hello World!'")

# Para liberar los buffers de red y asegurarnos de que el mensaje fue entregado simplemente
# cerramos la conexion
connection.close()
