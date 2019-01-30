# iworm

Proyecto desarrollado para la asignatura de sistemas operativos que consiste en la creación
de un gusano que se propague por la red local y consuma recursos del computador,
incluyendo en dicho codigo el uso de hilos.

Es importante destacar que el gusano usa como puerta de entrada a otras computadoras el servicio
de ssh, por lo que solo las computadoras corriendo dicho servicios y con el puerto 22 abierto se verán afectadas, además el gusano fue desarrollado especialmente para atacar equipos con sistema operativo linux.

El codigo correspondiente al gusano fue escrito en python y su funcionamiento se puede describir
sencillamente en los siguientes puntos:

-En la primera pc el atacante ejecuta el script, que comienza por escanear las ip de dispositivos
que se encuentran en la red local y verificar si tienen abierto el puerto 22 (correspondiente
al ssh).

-En caso de encontrar alguna pc con estas caracteristicas, se procede a realizar un ataque de fuerza bruta contra dicha pc hasta acceder a la misma mediante ssh.

-Durante 30 segundos, la pc infectada realizara el escaneo de puertos nuevamente para seguir buscando otras pc que no hayan sido infectadas y esten disponibles en la red local, e infectarlas de la misma manera anteriormente dicha.
 
-Pasados los 30 segundos el gusano empezara a consumir los recursos de esa pc lentamente, hasta lograr que la pc se cuelgue.

