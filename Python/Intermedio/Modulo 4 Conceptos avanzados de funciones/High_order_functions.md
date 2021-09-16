# Funciones de orden superior

es una funcion que recibe como paraetro a otra funcion

ejemplo

```python
def saludo(func):
    func()

def hola()
    print("Holaa)

def adios():
    print("adios" )
```
hay 3 funciones de orden superior:
-Filter
-Map
-Reduce

filter devuelve True or False según el valor esté dentro de los criterios buscados o no. En caso de que no cumpla con la condición, no será devuelto y la lista se verá reducida por este filtro.
Map funciona muy parecido, pero su diferencia radica en que no puede eliminar valores de la lista del array entregado. Es decir, el output tiene la misma cantidad de valores que el input.
Cómo funciona reduce:

Reduce toma 2 valores entregados como parámetros y el iterador como otro parámetro. Realiza la función con estos 2 valores, y luego con el resultado de esto y el valor que le sigue en el array. Y así hasta pasar por todos los valores de la lista.