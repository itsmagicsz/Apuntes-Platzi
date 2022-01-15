Básicos

De tipo: div {...}
De clase: .elemento {...}
De ID: #id-del-elemento
De atributo: a[href="..."]{...}
universal: *{...}

Combinadores

Descendientes: div p
Hijo directo: div > p
Elemento adyaente: div + p
General de hermanos: div ~ p

Los selectores nos ayudan a indicar el elemento sobre el que se van a aplicar los estilos. Existen muchos tipos de selectores y algunos de los más destacados son los que se detallan a continuación.

BASICOS DETALLES

-Selector universal

    Sintaxis: * { atributo:valor; }
    Ejemplo:* { color: grey; }/* El estilo se aplicará a todos los elementos de la página*/

-Selector etiqueta

    Sintaxis: etiqueta { atributo:valor }
    Ejemplo: p {color: green;}  /* El estilo se aplicará a todos los elementos <p>.*/

-Selector clase

    Sintaxis: .clase { atributo:valor }
    Ejemplo: .blend{color: red;} /* El estilo se aplicará a cualquier elemento que tenga la clase .blend */

-Selector identificador
El selector identificador utiliza el atributo id para seleccionar un elemento. Solo puede haber un elemento con un id dado en un documento.

    Sintaxis: #id { atributo:valor }
    Ejemplo: #cent {color: blue;} /* El estilo se aplicará al elemento que tenga el id #cent */

    

COMBINADORES DETALLES

-Selector descendiente :Un elemento es descendiente de otro cuando se encuentra entre las etiquetas de apertura y de cierre del elemento padre.

    Sintaxis: selector1 selector2 selectorN {atributo: valor;} /* El estilo se aplica sobre el selector N */
    Ejemplo: div p { color: black;} /* El estilo se aplica a todos los párrafos que se encuentren dentro de una etiqueta div */

-Combinación de selectores: La combinación de selectores nos permite dar un estilo a todos los selectores indicados.

    Sintaxis: selector1, selector2, selector3{atributo: valor;} /* El estilo se aplica sobre los selectores indicados */
    Ejemplo: div, p { color: orange;} /* El estilo se aplica a todos los divs y párrafos */

-Selector de hijos: Se usa para seleccionar un elemento que es hijo de otro elemento.

    Sintaxis: selector1 > selector2 {atributo: valor;}  /* El estilo se aplica sobre el selector 2 */
    Ejemplo: div > p { color: white;} /* El estilo se aplica a todos los párrafos que sean hijos de un div */

-Selector adyacente: Se usa para seleccionar elementos que son hermanos, es decir, su elemento padre es el mismo y están seguidos en el código HTML.

    Sintaxis: selector1 + selector2{ atributo: valor; } /* El estilo se aplica al selector 2 */
    Ejemplo: div + p { color: black;} /* El estilo se aplica a todos los párrafos que sean hermanos de un div */

