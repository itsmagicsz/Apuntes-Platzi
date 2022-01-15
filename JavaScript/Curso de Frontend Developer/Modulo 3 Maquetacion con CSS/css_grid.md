
TODO VA A CONTENER ESTO  -> garden {
                        display: grid;
                        grid-template-columns: 20% 20% 20% 20% 20%;
                        grid-template-rows: 20% 20% 20% 20% 20%;
                        }

grid-column-start: 3; regará el área comenzando por la tercera línea vertical, 
que es otra manera de decir el 3er borde vertical contando desde la izquierda de la cuadrícula.

Usando grid-column-end, riega todas las zanahorias evitando que se forme barro. ¡No queremos malgastar agua! Fíjate en que las zanahorias comienzan en el 1er borde vertical y terminan en el 4º.

    water {
    grid-column-start: 1;
    grid-column-end: span 3
    }


Al emparejar grid-column-start y grid-column-end, podrías asumir que el valor final tiene que ser mayor que el valor inicial. ¡Pero no es el caso!

Intenta establecer grid-column-end a un valor inferior a 5 para regar tus zanahorias.

    water {
    grid-column-start: 5;
    grid-column-end: 2
    }


Si prefieres contar las líneas de la cuadrícula comenzando por la derecha, puedes dar a grid-column-start y grid-column-end valores negativos. Por ejemplo, puedes establecerlos a -1 para indicar la primera línea comenzando por la derecha.

Intenta establecer grid-column-end a un valor negativo.

    water {
    grid-column-start: 1;
    grid-column-end: -2
    }


En lugar de definir un elemento en la cuadrícula basado en la posicion inicial y final, puedes definirlo basado en la longitud de columnas deseada usando la palabra clave span. Ten presente que span solo funciona con valores positivos.

Por ejemplo, riega las zanahorias usando grid-column-end: span 2;.

    water {
    grid-column-start: 2;
    grid-column-end: span 2;
    }


Escribir ambos grid-column-start y grid-column-end cada vez puede resultar cansado. Afortunadamente, grid-column es una propiedad abreviada que acepta ambos valores a la vez, separados por una barra oblicua.

Por ejemplo, grid-column: 2 / 4; establecerá el comienzo del elemento de la cuadrícula en la 2ª línea vertical de esta, y su final en la 4ª línea vertical.

    water {
    grid-column: 4/6;
    }


Intenta usar grid-column para regar las zanahorias. La palabra clave span también funciona con esta propiedad abreviada

    water {
    grid-column: span 3/5
    }

Una de las cosas que diferencia las cuadrículas de CSS de flexbox es que puedes posicionar los elementos 
fácilmente en 2 dimensiones: columnas y filas. grid-row-start funciona de manera semejante a 
grid-column-start pero a lo largo del eje vertical.

water {
grid-row-start: 3
}


Usa grid-column y grid-row a la vez para establecer una posición en ambas dimensiones.

    poison {
    grid-column-start: 2;
    grid-row-start:5
    }

Si escribir grid-column y grid-row se te hace demasiado pesado, aquí tienes otra propiedad abreviada. grid-area admite cuatro valores separados por barras oblicuas: grid-row-start, grid-column-start, grid-row-end, seguido de grid-column-end.

    water {
    grid-area: 1 / 2 / 4 / 6;
    }

¿Y qué me dices de múltiples elementos? Puedes superponerlos sin problema. Usa grid-area para definir una segunda área que cubra todas las zanahorias que están sin regar.

    water-1 {
    grid-area: 1 / 4 / 6 / 5;
    }

    water-2 {
    grid-area: 2 / 3 / 5 /6 ;
    }