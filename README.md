# RabbitMQ
1.- En la primera parte por medio de un programa en python enviamos un mensaje a la pila y la consumimo otro programa en python

2.-En la segunda parte muestra como distribuir las tareas de una cola de alto consumo de tiempo entre varios workers.

3.- En la tercera parte se trata del patron publicador/suscriptor, en donde el publicador emite un mensaje y todos los publicadores pueden ver ese mensaje. Los mensajes emitidos por un programa producer no se envian directamente a una cola, sino que pasa atraves de un exchange (hay varios tipos de exchange), el que usamos en este ejercicio es el fanout que envia el mensaje a todas las colas conocidas. en el programa consumer crea una cola cuyo nombre aleatorio es generado por RabbitMQ y que hace referencia al exchange. De esta manera todos los programas consumers que hagan referencia a este exchange recibiran en sus colas dicho mensaje.

4.- En esta parte el exchange (tipo direct) puede filtrar los mensajes que enviara a la(s) cola(s), Esto se hace con el parametro routing_key cuando se crea el binding (vinculo de exchange con la cola), en donde al consumer se le indica cual tipo de mensajes debe recibir.

5.- En este caso se trata de que el exchange haga filtrados mas complejos, este tipo de exchange es el topic. Los criterios se excriben a elegir se escriben en el programa producer. Estos criterios se escriben separandolos por punto y con un maximo de 255 caracteres. se usa * para denotar que un criterio dado puede ser cualquiera y se escribe # para denotar que puede recibir varios criterios ejemplo.

criterio1.* solamente seran filtradas las cadenas que tengan criterio1, punto y posteriormente un criterio mas que puede ser cualquier cadena.

criterio1.# solamente seran filtradas las cadenas que tengan criterio1, punto y posteriormente cualquier numero de criterios separado por punto y estos pueden ser cualquier cadena.


