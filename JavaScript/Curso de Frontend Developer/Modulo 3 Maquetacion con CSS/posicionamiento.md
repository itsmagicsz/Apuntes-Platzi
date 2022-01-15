Propiedades de posicionamiento CSS

    top.- establece la distancia superior, del elemento respecto a otro.
    left.- establece la distancia por el lado derecho del elemento respecto a otro.
    bottom.- distancia inferior de un elemento respecto a otro.
    right.- distancia por el lado izquierdo de un elemento respecto a otro.
    ksnip_20211005-114323.png
    Valores para la propiedad position

    estatic.- la forma por defecto, obedece al flujo normal de la página.
    relative.- establece que la posición de un elemento depende de otro.
    absolute.- indica que la posición de un elemento no depende de otro.
    fixed.- permite fijar un elemento en una posición determinada.
    inherit.- hereda el estilo de posición del elemento padre.

Posicionamiento relativo (relative)
El valor relative para la propiedad position de CSS, establece que el elemento
será posicionado relativo a su posición normal o inicial y sus características más destacadas son:

Los elementos con posición relativa se encuentran el espacio original que ocupaban.
El valor relativesaca al elemento del flujo normal para que quede posicionado con propiedades de posicionamiento.
Ahora tiene sentido establecer las propiedades: arriba, derecha, abajo o izquierda para indicar cuánto y dónde se desplazan los elementos.
El elemento será desplazado tomando en cuenta a su posición original como punto de partida.
Los elementos posicionados con relative pueden superponerse a otros.
Posicionamiento absoluto (absolute)

El posicionamiento absoluto de elementos con CSS posee características que lo diferencian de las otras formas de posicionamiento y eso es lo que vamos a conocer y practicar en esta sección.

El valor absolute para la propiedad position establece que un elemento debe ser posicionado de forma absoluta y básicamente se comporta de la siguiente manera:

El elemento es removido del flujo normal de contenido para ser posicionado mediante las propiedades de posicionamiento.
Una vez removido no conserva el espacio que ocupaba originalmente, es decir los demás elementos se comportan como si el elemento posicionado como absoluto no existiera.
Elementos posicionados como absoluto pueden superponerse sobre los demás elementos.
En el posicionamiento absoluto, los elementos se posicionan respecto al elemento padre más cercano que tenga establecido una forma de posicionamiento (position) distinto al por defecto o static.
Posicionamiento fijo (fixed)
El posicionamiento fijo de elementos en CSS consiste en establecer una posición determinada para un elemento, de tal manera que queda fija y no se mueva de dicha posición, aun cuando se hace scroll en la pantalla.

Para establecer una posición fija, se emplea el valor fixed para la propiedad position.

Características de un elemento con position: fixed

Los elementos posicionados con valor fixed salen del flujo normal para ser posicionados con las propiedades de posicionamiento.
El espacio original que ocupaba un elemento desaparece una vez establecida la posición fija, por ende los demás elementos se comportan como si no existiera.
El elemento se posiciona respecto a los límites de la pantalla, es decir el punto de partida es el borde de pantalla.
Quedan fijas en una posición determinada y no pueden moverse aunque el usuario se desplace por la pantalla.
Elementos fijados pueden superponerse sobre otros.