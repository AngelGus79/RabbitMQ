import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()
# El Produce no envia directamente mensajes a las colas, sino
# que pasa por un exchange, este exchange redirecciona el mensaje
# a la(s) colas  basado en varios criterios (¿Deberia agregarse
# a una cola especifica?, ¿Deberia agregarse a varias colas?,
# ¿Deberia descartar mensajes?) esto depende del tipo de cola.
# en los ejemplos anteriores habiamos visto exchanges que asignaban
# los mensajes a una cola especifica. El siguiente tipo de exchange
# redirije todos los mensajes a todas las colas que el conoce.
channel.exchange_declare(exchange='logs',
                         type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)
print(" [x] Sent %r" % message)
connection.close()
