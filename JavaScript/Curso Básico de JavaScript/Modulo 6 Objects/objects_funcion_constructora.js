function auto(marca, modelo, annio) {  // Creas una función con los parametros que va a recibir, 
    this.marca = marca;   // Utilizamos el "this" para asignar valores a las propiedades del objeto 
    this.modelo = modelo;
    this.annio = annio;
}

var newAuto = new auto("Tesla", "Model 3", 2020);

var newAuto2 = new auto("Ferrari", "Model 10", 2015);

newAuto //imprime los valores que estan dentro de newAuto
newAuto2 //imprime los valores que estan dentro de newAuto2



