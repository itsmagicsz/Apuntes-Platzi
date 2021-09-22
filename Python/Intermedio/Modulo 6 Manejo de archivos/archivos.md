 # Como trabajar con archivos?

 Hay diferentes tipos de arcchivos: 
 - Archivos de texto: Tienen bytes que por dentro que representan letras, numeros, simbolos, etc . 
 EJEMPLO: .txt, .css, .xml, .json, .py, .js, .csv

 - Archivos binarios: Tienen bytes que por dentro representan cosas mas complejas, como datos especificos de imagenes, etc 
 EJEMPLO : .png, .mp3, .jpg, .avi, .dll, .mp4

Para abrir un archvio de texto con pythonn vamos a encontrar tres formas de hacerlo:
- r -> Lectura 
- w -> Escritura(sobreescribir sobre ese mismo archivo)
- a -> Escritura(agregar al final)

with open( "./ruta/del/archivo.txt", "r") as f :

with : Es un manejador contextual , lo que hace es controlar el flujo de nuestro archivo 

##### Modos de apertura

r -> Solo lectura
r+ -> Lectura y escritura
w -> Solo escritura. Sobre escribe el archivo si existe. Crea el archivo si no existe
w+ -> Escritura y lectura. Sobre escribe el archivo si existe. Crea el archivo si no existe
a -> Añadido (agregar contenido). Crea el archivo si éste no existe
a+ -> Añadido (agregar contenido) y lectura. Crea el archivo si éste no existe.
