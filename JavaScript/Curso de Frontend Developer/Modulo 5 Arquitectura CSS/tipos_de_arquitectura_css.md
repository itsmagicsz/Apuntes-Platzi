ARQUITECTURAS CSS 📐📏
.
.
.
🟢OOCSS(oriented object cascading style sheets)
Optimiza nuestro código para reducirlo y poder agregar más código de una forma rápida.
.
Para nuestro ejemplo creamos dos cajas con las mismas propiedades pero de diferente color…

//HTML
<div class="caja1"></div>
<div class="caja2"></div>
//CSS
.caja1 {
  background: 🟦blue;
  width: 200px;
  height: 200px;
}
.caja2 {
  background: 🟥red;
  width: 200px;
  height: 200px;
}
el problema aquí es que estamos repitiendo el código CSS para las 2 cajas cuando solo queremos cambiar de color.
La solución a esto es crear una clase que contenga la estructura de ambas cajas.

//HTML 
<div class="caja azul"></div>
<div class="caja roja"></div>
//CSS
.caja {
  width: 200px;
  height: 200px;
}
.azul {
  background: 🟦blue;
}
.roja {
  background: 🟥red;
}
Como puedes ver la clase “.caja” es la que contiene toda la estructura y con las demás clases “.azul🟦”, “.roja🟥” le damos color a nuestras cajas.
.
OOCSS se utiliza en todos lados y su uso mas cercano está en los Frameworks de diseño web, tal como boostrap, fundation, etc.

🟢BEM(Block, Element, Modifier)
Es una convención o metodología para nombrar tus clases de CSS.
Sirve:
*Para tener un CSS más fácil de leer, entender, mantener y escalar.
*Para organizar las clases de CSS en módulos independientes.
*Para evitar selectores de CSS anidados.
.
-Bloque: es el contenedor principal del componente.(card, button, form, menu, header…)
-Elemento: son las partes internas que conforman el componente.( icon, text, item, image, input, button…)
-Modificador: son las variaciones del bloque o del elemento.(active, big, right, secondary, red…)
.
Los nombres de clases con convención BEM, pueden tener la siguiente sintaxis:

[bloque]
[bloque]__[elemento]
[bloque]--[modificador]
[elemento]--[modificador]
[bloque]__[elemento]--[modificador]
Los guiones bajos (__) se usan para separar el bloque del elemento,
Los guiones medios (–) se usan para separar el bloque o el elemento del modificador.

https://platzi.com/blog/bem/


🟢SMACSS(Arquitectura escalable y modular para CSS)
*Es una guía de estilo que sigue cinco categorías simples.
*Es una forma de examinar su proceso de diseño y adaptar esos marcos rígidos a un proceso de pensamiento flexible.
*Es un intento de documentar un enfoque coherente para el desarrollo del sitio cuando se utiliza CSS.

La idea de esta arquitectura es no mezclar código de varias categorías en un solo archivo porque puede ser muy complicado encontrar una línea de código simple para cambiar. La mayor parte del propósito de esta categorización es codificar patrones, cosas que se repiten dentro de nuestro diseño. La repetición resulta en menos código, mantenimiento más fácil y mayor consistencia en la experiencia del usuario.

¿Cuáles son estas categorías?
-Base: son los valores predeterminados. Son como el relleno, el margen, el borde, la fuente y otras propiedades, estos valores se utilizan en todo el sitio web y todos los elementos.
.
-Layout: divide una página en secciones con elementos como encabezado, pie de página, página principal, etc. Los diseños mantienen uno o más módulos juntos.
.
-Modules: son las partes reutilizables y modulares de nuestro diseño, como la barra de navegación, la barra lateral y algunos elementos que se repiten en el sitio.
.
-State: son formas de describir cómo se verán nuestros módulos o diseños cuando estén en un estado particular (por ejemplo, activo, inactivo, expandido, oculto).
.
-Theme: Las reglas de tema son similares a las reglas de estado en que describen cómo podrían verse los módulos o diseños. -

ITCSS( Inverted Triangle CSS)
Arquitectura CSS del triángulo invertido es una arquitectura escalable y manejable para el CSS. Básicamente son una serie de normas o planteamientos para crear el CSS, como una filosofía.
.
Ayuda a organizar los archivos CSS de su proyecto de tal manera que pueda manejar mejor los aspectos específicos de CSS, como el espacio de nombres global, la cascada y la especificidad de los selectores .


🟢Atomic Design
Es un sistema de trabajo que se basa en la creación de elementos modulares sencillos para crear estructuras de información mucho más complejas.
Cada vez tenemos que diseñar para más tamaños de pantallas y para distintos dispositivos (móviles, tabletas, TV, etc.) y necesitamos procesos que eviten errores y faciliten el desarrollo.