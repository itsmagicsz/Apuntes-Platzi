1️⃣ Responde las siguientes preguntas en la sección de comentarios:

¿Qué es una variable y para qué sirve?
¿Cuál es la diferencia entre declarar e inicializar una variable?
¿Cuál es la diferencia entre sumar números y concatenar strings?
¿Cuál operador me permite sumar o concatenar?

-Es un espacio que se reserva en la memoria el cual nos permite almacenar datos
-Declarar prepara el espacio en la memoria que sera utilizada, mientras que inicializar la variable ya le da un valor a dicho espacio
-Sumar numeros suma valores numeroricos dejando solo un resultado y concatenar strings es tener dos o mas valores tipo string y unirlos para formar un solo valor
-El operador + 

2️⃣ Determina el nombre y tipo de dato para almacenar en variables la siguiente información:

2️⃣ Determina el nombre y tipo de dato para almacenar en variables la siguiente información:

Nombre
var nombre (tipo string)

Apellido
var apellido (tipo string)

Nombre de usuario en Platzi
var nickName (tipo string)

Edad
var edad (tipo int)

Correo electrónico
var email (tipo string)

Mayor de edad
var mEdad (tipo boolean)

Dinero ahorrado
var ahorros (tipo float o double)

Deudas
var deudas (tipo float o double)

3️⃣ Traduce a código JavaScript las variables del ejemplo anterior y deja tu código en los comentarios.

var nombre = 'Juan Fra'
var apellido = 'Ruano'
var nickName = 'Pinguino'
var edad = 23
var email = 'juan.francisco.45@hotmail.com'
var mEdad = true
var ahorros = 900.00
var deudas = 70.00

4️⃣ Calcula e imprime las siguientes variables a partir de las variables del ejemplo anterior:

Nombre completo (nombre y apellido)

var nombreCompleto = nombre + ' ' + apellido o `${nombre} ${apellido}`

Dinero real (dinero ahorrado menos deudas)

var dReal = ahorros - deudas

FUNCIONES

1️⃣ Responde las siguientes preguntas en la sección de comentarios:

¿Qué es una función?
Un bloque de codigo que cumple con una tarea especifica

¿Cuándo me sirve usar una función en mi código?
Cuando encontramos una tarea que se repite varias veces en el codigo, podemos hacerla funcion y simplemente la invocamos cuando se necesite

¿Cuál es la diferencia entre parámetros y argumentos de una función?
Los parametros son variables dentro de la funcion misma mientras que los argumentos son variables que nosotros enviamos a la funcion al momento de invocarla

2️⃣ Convierte el siguiente código en una función, pero, cambiando cuando sea necesario las variables constantes por parámetros y argumentos en una función:

const name = "Juan David";
const lastname = "Castro Gallego";
const completeName = name + lastname;
const nickname = "juandc";

console.log("Mi nombre es " + completeName + ", pero prefiero que me digas " + nickname + ".");

//con funcion 

const quienSoy = (nombres, apellidos, nickname) => {
    var nombreCompleto = `${nombres} ${apellidos}`
    console.log(`Mi nombre es ${nombreCompleto}, pero prefiero que me digas ${nickname}.`)
}

quienSoy("Juan Fra","Ruano","Pinguino")

CONDICIONALES

1️⃣ Responde las siguientes preguntas en la sección de comentarios:

¿Qué es una condicional?
Un bloque de codigo que se ejecuta en caso de que se cumpla una condicion o pregunta lógica

¿Qué tipos de condicionales existen en JavaScript y cuáles son sus diferencias?
if, else if, switch, ternario

¿Puedo combinar funciones y condicionales?
Si

2️⃣ Replica el comportamiento del siguiente código que usa la sentencia switch utilizando if, else y else if:


const tipoSuscripcion = (suscripcion) =>{
    if(suscripcion === 'Basic'){
        console.log("Puedes tomar casi todos los cursos de Platzi durante un mes");
    }
    else if(suscripcion === 'Expert'){
        console.log("Puedes tomar casi todos los cursos de Platzi durante un año");
    }
    else if(suscripcion === 'Expert+'){
        console.log("Tú y alguien más pueden tomar TODOS los cursos de Platzi durante un año");
    }
    else {
        console.log("Solo puedes tomar los cursos gratis");
    }
}

tipoSuscripcion('Basic')
3️⃣ Replica el comportamiento de tu condicional anterior con if, else y else if, pero ahora solo con if (sin else ni else if).

const tipoSuscripcion = (suscripcion) =>{
    var respuesta = suscripcion === 'Basic' ? "Puedes tomar casi todos los cursos de Platzi durante un mes": 
                        suscripcion === 'Expert' ? "Puedes tomar casi todos los cursos de Platzi durante un año":
                            suscripcion === 'Expert+' ? "Tú y alguien más pueden tomar TODOS los cursos de Platzi durante un año" : "Solo puedes tomar los cursos gratis"
    console.log(respuesta)
}

tipoSuscripcion('Basic')
Bonus: si ya eres una experta o experto en el lenguaje, te desafío a comentar cómo replicar este comportamiento con arrays y un solo condicional. 😏


const tiposSuscripciones = ['Free','Basic','Expert','Expert+']
const descSuscripciones = ['Solo puedes tomar los cursos gratis','Puedes tomar casi todos los cursos de Platzi durante un mes','Puedes tomar casi todos los cursos de Platzi durante un año','Tú y alguien más pueden tomar TODOS los cursos de Platzi durante un año','No existe dicha suscripcion']

const tipoSuscripcion = (suscripcion) =>{
    posicion = tiposSuscripciones.indexOf(suscripcion)==-1 ? 4 : tiposSuscripciones.indexOf(suscripcion)
    var respuesta =  descSuscripciones[posicion]
    console.log(respuesta)
}
tipoSuscripcion('Basic')

CICLOS

1️⃣ Responde las siguientes preguntas en la sección de comentarios:

¿Qué es un ciclo?
Es un bloque de codigo que se repite n cantidad de veces hasta que se cumpla una condicion

¿Qué tipos de ciclos existen en JavaScript?
while, do while, for

¿Qué es un ciclo infinito y por qué es un problema?
Cuando un ciclo no cumple su condicion, consume mucho la memoria del computador o buscador y puede generar colapsos en el sistema o volverlo lento

¿Puedo mezclar ciclos y condicionales?
Si, incluso los ciclos utilizan condicionales para funcionar de forma adecuada

2️⃣ Replica el comportamiento de los siguientes ciclos for utilizando ciclos while:

var i = 0
while(i < 5){
    console.log("El valor de i es: " + i);
    i++;
}
i+=5 
while(i>=2){
    console.log("El valor de i es: " + i);
    i--;
}
3️⃣ Escribe un código en JavaScript que le pregunte a los usuarios cuánto es 2 + 2. Si responden bien, mostramos un mensaje de felicitaciones, pero si responden mal, volvemos a empezar.

var solucion = 0
do{
    solucion = Number(prompt('Cuanto es 2+2?'))
}while(solucion!==4)
LISTAS

1️⃣ Responde las siguientes preguntas en la sección de comentarios:

¿Qué es un array?
Es una cadena de datos agrupados en una variable

¿Qué es un objeto?
Es un grupo de propiedades

¿Cuándo es mejor usar objetos o arrays?
Depende de lo que se requiera

¿Puedo mezclar arrays con objetos o incluso objetos con arrays?
Si

2️⃣ Crea una función que pueda recibir cualquier array como parámetro e imprima su primer elemento.

const tiposSuscripciones = ['Free','Basic','Expert','Expert+']

const primerElemento = (array) => console.log(`El primer elemento del array es ${array[0]}`)

primerElemento(tiposSuscripciones)
3️⃣ Crea una función que pueda recibir cualquier array como parámetro e imprima todos sus elementos uno por uno (no se vale imprimir el array completo).

const tiposSuscripciones = ['Free','Basic','Expert','Expert+']

const elementos = (array) => array.forEach((elemento,index) => console.log(`El elemento ${index} del array es ${elemento}`))

primerElemento(tiposSuscripciones)
4️⃣ Crea una función que pueda recibir cualquier objeto como parámetro e imprima todos sus elementos uno por uno (no se vale imprimir el objeto completo).

var estudiante = {
    nombre:'Juan',
    apellido:'Ruano',
    edad:23,
    trabajando:false
}

const datosEstudiante = (objeto) => {
    for(var prop in objeto){
        console.log(`La propiedad ${prop} tiene como valor ${objeto[prop]}`)
    }
}

datosEstudiante(estudiante)