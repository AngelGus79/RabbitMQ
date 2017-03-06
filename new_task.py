#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

# Si el servidor de RabbitMQ se cae, este olvidara las colas a menos que se
# configure la cola y el mensaje para que no pase asi.
# para la cola: configurar el parametro durable = True en su declaracion
# Para el mensaje poner el parametro delivery_mode = 2.
# ojo si ya se declaro una cola sin haberse establecido como durable=True desde
# el principio, RabbitMQ no permite reconfigurarse, se debera poner otro nombre
# de cola.

channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=message,
                      properties=pika.BasicProperties(
                         delivery_mode = 2, # make message persistent
                      ))
print(" [x] Sent %r" % message)
connection.close()
