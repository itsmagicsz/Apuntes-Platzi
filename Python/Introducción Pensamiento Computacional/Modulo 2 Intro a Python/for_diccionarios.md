Bucles for con diccionarios
Para iterar a lo largo de un diccionario tenemos varias opciones:

Ejecutar el bucle for directamente en el diccionario, lo cual nos permite
iterar a lo largo de las llaves del diccionario.
Ejecutar el bucle for en la llamada keys del diccionario, lo cual nos permite
iterar a lo largo de las llaves del diccionario.
Ejecutar el bucle for en la llamada values del diccionario, lo cual nos
permite iterar a lo largo de los valores del diccionario.
Ejecutar el bucle for en la llamada items del diccionario, lo cual nos
permite iterar en una tupla de las llaves y los valores del diccionario.

estudiantes = {
    'mexico': 10,
    'colombia': 15,
    'puerto_rico': 4,
}

for pais in estudiantes:
    ...

for pais in estudiantes.keys():
    ...

for numero_de_estudiantes in estudiantes.values():
    ...

for pais, numero_de_estudiantes in estudiantes.items():
    ...