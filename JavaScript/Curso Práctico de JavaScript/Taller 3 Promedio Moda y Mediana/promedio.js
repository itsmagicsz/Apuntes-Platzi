function calcularMediaAritmetica(lista) {
    // let sumaLista = 0;
    // for (let i = 0; i < lista.length; i++) {
    //   sumaLista = sumaLista + lista[i];
    // }

    var lista = [];
  
    const sumaLista = lista.reduce(
      function (valorAcumulado = 0, nuevoElemento) {
        return valorAcumulado + nuevoElemento;
      }
    );
  
    const promedioLista = sumaLista / lista.length;
  
    return promedioLista;
  }

function onClickbuttonAverage(){
    const inputPromedio = document.getElementById("InputPromedio");
    const promedioValue = inputPromedio.value;

    const promedio = calcularMediaAritmetica(promedioValue);

    const resultPromedio = document.getElementById("ResultPromedio");
    resultPromedio.innerText = "El promedio de la lista de numeros es " + promedio;
  }
