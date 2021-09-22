# Manejo de excepciones

try except → Anidamos nuestro programa en dos bloques de código, el primero es el programa per se (el que se ejecuta normalmente, sin errores) y el segundo representa las instrucciones a seguir en caso de error.
Su sintaxis es:
try:
	<bloque1>
except <error> as <alias>:
	<bloque 2>

<error> es un parámetro opcional, permite capturar sólo el tipo de error indicado, si no se coloca captura todos los errores posibles (es buena práctica capturar cada tipo de error por separado)

as <alias> nos permite crear un alias al error, para trabajar con él.

raise → Esta instrucción nos permite generar errores, es decir crear nuestros propios errores cuando detectemos que nuestro programa no actúa como debería con cierto tipo de datos
Su sintaxis es:
	raise <NombreError>("<descripci[on del error>")

fynally → Es una bloque de código que se ejecuta exista un error o no (un tercer bloque después de try except), no es muy usual pero puede darse para cerrar archivos, conexiones a BBDD o liberar recursos