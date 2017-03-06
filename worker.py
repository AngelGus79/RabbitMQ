#!/usr/bin/env python
import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
# Con la siguiente linea le decimos a rabbitMQ que cada mensaje que sea
# enviado, el consumidorun ack se le devuelve a rabbit para informarle
# que el mensaje fue recibido, procesado y que ya puede ser eliminado.
    ch.basic_ack(delivery_tag = method.delivery_tag)



# En caso de que las tareas pesadas esten en posicion para
# y tareas livianas en posicion par uno de los trabajadores
# estara trabajando muy poco, esta carga puede ser mas
# equitativa si se configura el parametro prefetch_count = 1
# para de esta forma decirle a RabbitMQ que no le asigne una tarea
# a un worker si esta ocupado, en vez de esto asignarsela al
# que este desocupado.
channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='task_queue')

channel.start_consuming()
