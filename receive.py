import pika

#Para consumir el mensaje, creamos la conexion
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

# Este paso se podria omitir si estamos seguros de que existe la cola, pero aun asi
# es buena practica validarlo con la misma linea de codigo con la cual se declara.
channel.queue_declare(queue='hello')

# suscribimos la funcion callback a la cola, cuando se reciba un mensaje esta funcion
# es llamada por la libreria  pika
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

# Luego le decimos a rabbit que esta funcion (callback) va a recibir los mensajes de la cola,
# obvio para que tenga exito esta funcion la cola debe existir
channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)
print(' [*] Waiting for messages. To exit press CTRL+C')
# Con esta instruccion entramos en un ciclo en espera de datos y de que se ejecute la funcion callback
# cuando sea necesario
channel.start_consuming()
