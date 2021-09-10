# Entorno virtual

la idea es sencilla, de hecho el concepto es similar al de los contenedores de Docker, como profesional empezarás a requerir de trabajar diversos proyectos que trabajen con diferentes versiones, ya sea del lenguaje o de algún módulo.
.
Sería una catástrofe tener que instalar y actualizar módulos para cada proyecto cuidando que ninguno se rompa, porque fácilmente podrías actualizar un módulo que, para un proyecto funcione, pero para otro deje de funcionar, es por eso que se crea el concepto de entornos virtuales.
.
Este concepto lo tienen muchos lenguajes, y lo genial es que soluciona muy bien el problema de la compatibilidad entre proyectos, porque cada entorno virtual es independiente y funciona con las versiones que se les hayan instalado ahí mismo 😄.

Un entorno virtual es un directorio que contiene una instalación de Python de una versión en particular, además de unos cuantos paquetes adicionales.