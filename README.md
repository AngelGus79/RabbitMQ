# RabbitMQ
1.- En la primera parte por medio de un programa en python enviamos un mensaje a la pila y la consumimo otro programa en python

2.-En la segunda parte muestra como distribuir las tareas de una cola de alto consumo de tiempo entre varios workers.

3.- En la tercera parte se trata del patron publicador/suscriptor, en donde el publicador emite un mensaje y todos los publicadores pueden ver ese mensaje. Los mensajes emitidos por un programa producer no se envian directamente a una cola, sino que pasa atraves de un exchange (hay varios tipos de exchange), el que usamos en este ejercicio es el fanout que envia el mensaje a todas las colas conocidas. en el programa consumer crea una cola cuyo nombre aleatorio es generado por RabbitMQ y que hace referencia al exchange. De esta manera todos los programas consumers que hagan referencia a este exchange recibiran en sus colas dicho mensaje.

4.- En esta parte el exchange (tipo redirect) puede filtrar los mensajes que enviara a la(s) cola(s), Esto se hace con el parametro routing_key cuando se crea el binding (vinculo de exchange con la cola), en donde al consumer se le indica cual tipo de mensajes debe recibir.
