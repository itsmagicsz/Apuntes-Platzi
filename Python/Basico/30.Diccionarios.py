#DICCIONARIOS

#Son una estructura de datos mutable las cuales almacenan 
# diferentes tipos de valores sin darle importancia a su orden.
# Identifican a cada elemento por una clave (Key). Se escriben entre {}.


def run():

    mi_diccionario = {
        "llave1" : 1,
        "llave2" : 2,
        "llave3" : 3,
    }

    #print(mi_diccionario)

    #print(mi_diccionario["llave1"])
    #print(mi_diccionario["llave2"])
    #print(mi_diccionario["llave3"])

    poblacion_paises = {
        "Argentina" : 44938712,
        "Brazil " : 210147125,
        "Colombia " : 50372424
    }

    #print(poblacion_paises["Argentina"])

    #for pais in poblacion_paises.keys(): #Este devuelve solo los nombres de la llaves
    #   print(pais)

    #for pais in poblacion_paises.values():  #Este devuelve solo el valor de la llaves
    #   print(pais)

    for pais, poblacion in poblacion_paises.items(): #Este devuele los dos valores el nombre y el valor de las llaves
        print(pais + " tiene " + str(poblacion) + " habitantes " )
    
    



if __name__ == "__main__":
    run()

