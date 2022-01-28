//Codigo del cuadrado
console.group("Cuadrado")

//const ladoCuadrado = 5;
//console.log("Los lados del cuadrado miden " + ladoCuadrado + "cm")

function perimetroCuadrado(lado){
    return lado * 4;
}
perimetroCuadrado()
//console.log("El perimetro del cuadrado es " + perimetroCuadrado + "cm")

function areaCuadrado(lado){
    return lado * lado;
}
perimetroCuadrado()

//console.log("El area del cuadrado es " + areaCuadrado + "cm^2")

console.groupEnd();

//Codigo del triangulo
console.group("Triangulo")

// const ladoTriangulo1 = 6;
// const ladoTriangulo2 = 6;
// const baseTriangulo = 4;

// console.log(
//     "Los lados del triangulo miden " 
//     + ladoTriangulo1 + "cm, " 
//     + ladoTriangulo2 + "cm, " 
//     + baseTriangulo + "cm "
//     );

// const alturaTriangulo = 5.5;
// console.log("La altura del triangulo es de: " + alturaTriangulo + "cm")

function perimetroTriangulo(lado1, lado2, base){
    return lado1 + lado2 + base;
}

//console.log("El perimetro del triangulo es " + perimetroTriangulo + "cm")

function areaTriangulo(base,altura){
    return (base * altura) / 2
}

//console.log("El area del triangulo es " + areaTriangulo + "cm^2")

console.groupEnd();

//Código del círculo
console.group("Círculos");

//Radio
const radioCirculo = 4;


//Diametro

function diametroCirculo(radio){
    return radio *2
}

// PI
const PI = Math.PI;
console.log("PI es "+ PI + "cm")

//Circunferencia
function perimetroCirculo(radio){
    const diametro = diametroCirculo(radio)
    return diametro * PI
} 


//Area
function areaCirculo (radio){
    return (radio * radio) * PI;
} 

console.groupEnd();

// Aquí interactuamos con el HTML
function calcularPerimetroCuadrado() {
    const input = document.getElementById("InputCuadrado");
    const value = input.value;
  
    const perimetro = perimetroCuadrado(value);
    alert(perimetro);
  }
  function calcularAreaCuadrado() {
    const input = document.getElementById("InputCuadrado");
    const value = input.value;
  
    const area = areaCuadrado(value);
    alert(area);
  }

