PIP=  Package Installer Python = Paquete de instalador para python

Pip Nos permite descargar paquetes(modulos) de terceros para utilizarlos en nuestro enviroment, ademas se puede definir una versión especifica del paquete.

Modulos populares
-Requests
-BeautifulSoup4
-Pandas
-Numpy
-Pytest

COMANDOS

-pip freeze -> muestra todos los paquetes(modulos) instalados en tu ambiente virtual

-pip install <paquete(modulo)> -> instala el paquete(pandas , matplotlib, bokeh, etc) que se especifique

Si quisiéramos que alguien mas pueda ejecutar nuestro proyecto es importante compartir que librería y versión hemos empleado; eso se realiza con el comando:

-pip freeze > requirements.txt 
                                
lo que hace el archivo requirement.txt va a guardar las dependencias con sus respectivas versiones para poder compartirlo con otra persona

cuando esa persona quiera descargar ese proyecto tendra que utilizar el comando:

-pip install -r requirements.txt 