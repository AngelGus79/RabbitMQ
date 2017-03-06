import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         type='fanout')

# Cuando sea que nos conectemos RabbitMQ Necesita una nueva cola vacia,
# para lograr esto podriamos crear una cola con nombre aleatorio, pero
# esto lo puede hacer RabbitMQ por nosotros con la siguiente linea.
# Posteriormente una vez que desconectemos al cliente la cola deberia ser
# eliminada. Hay una bandera exclusiva para esto exclusive

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

# Hemos creado un exchange fanout y una cola, ahora necesitamos decirle al
# exchange que envie los mensajes a la cola. Esta relacion se llama binding
channel.queue_bind(exchange='logs',
                   queue=queue_name)

#Hasta este punto el exchange logs agregara mensajes a la cola.
print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r" % body)

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()
