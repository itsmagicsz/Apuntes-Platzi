Diccionario: En los diccionarios los datos se encierran entre { }, 
Un diccionario es una estructura de datos y un tipo de dato en Python con caracateristicas especiales que
 nos permiten alcenar cualquier valor ya sea int, float, booleano, string, listas, funciones. Estos se identifican por una clave (Key)

Uso del diccionario: Para definir un diccionario, se encierra el listado de valores entre llaves. 
Las parejas de clave y valor se separan con comas, y la clave y el valor se separan con dos puntos


diccionario = {'nombre' : 'jose', 'edad' : 26, 'cursos': ['Python','Django','JavaScript'] }
–> Podemos acceder al elemento de un Diccionario mediante la clave de este elemento, como veremos a continuación:

print diccionario['nombre'] #jose
print diccionario['edad']#26
print diccionario['cursos'] #['Python','Django','JavaScript']

Dictionary Comprehension es un metodo que te permite crear un nuevo diccionario apartir 
de un diccionario ya existente, y poder modificar las llaves y valores de acuerdo a tus necesidades, la sintaxis es:

my_dict={'Juan' : 20, 'Ana': 30, 'Arturo' : 45}

Nuevo_dict = {k:v for (k:v) in my_dict.items() if v<40}