Con la propiedad box-sizing: border-box; css busca que todo el elemento mida 
lo que indicamos en width y height, esto con ayuda del padding y el border,
de tal manera que se le resta espacio al content para poder lograr las dimensiones específicadas.

Esto es un tema muy mindblow 🤯. Básicamente porque todo en HTML son cajitas, sí, incluso un texto es una caja. Cuando tú insertas un texto, lo que estás haciendo es que estás insertando una cajita que adentro tiene texto (y lo mismo aplica para cualquier etiqueta). Esta cajita tiene un fondo transparente, pero si tú le pones cualquier fondo usando la propiedad background podrás ver esa cajita. Esta cajita, además de su contenido, tiene estas 3 capas externas que serían el padding, el border y el margin 👇:
.

padding: Es básicamente el espaciado que hay entre la caja y el contenido de la caja, es un espaciado interno. Lo solemos usar mucho para permitir que los elementos “respiren”, por ejemplo, aquí les dejo una comparación de un botón sin padding y uno con padding 👇

border: Es el delineado que le podemos dar a una caja, y un borde puede ser tan grueso como quieras. Simplemente debemos ponerle el grosor, el tipo de borde y el color del borde, por ejemplo, podemos hacer una caja con bordes y líneas intermitentes 

margin: Este es básicamente el espaciado entre elementos. Es la distancia que podemos dejar de un elemento hacia otro.

Y de ahora en adelante cuando empieces a desarrollar, notarás que muchos usan esto en CSS 👇:
.

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
.
Básicamente usan el selector universal para aplicarle a toooooodas las etiquetas estas propiedades (es decir, resetean estas propiedades, porque por defecto, el navegador le pone ciertos estilos 😄), pero tú ahora ya sabes cómo funcionan 👀.