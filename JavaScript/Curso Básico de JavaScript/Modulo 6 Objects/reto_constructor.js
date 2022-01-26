function auto (marca, modelo, anio){
  this.marca = marca;
  this.modelo = modelo;
  this.annio = anio;
}

var numeroautos = prompt("Ingresa la cantidad de autos que quieres");

var autos = [];
for(let i = 0 ; i < numeroautos ; i++){
  var marca = prompt("Ingresa la marca del auto");
  var modelo = prompt("Ingresa el modelo del auto");
  var annio = prompt("Ingresa el año del auto");
  autos.push(new auto (marca, modelo, annio));
}

for(let i = 0 ; i < autos.length ; i++){
  console.log(autos[i]);
}