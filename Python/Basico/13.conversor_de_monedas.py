def conversor(tipo_pesos, valor_dolar):
    pesos = input("How many" + tipo_pesos + "pesos do you have? ")
    pesos = float(pesos)
    dolares= pesos / valor_dolar
    dolares = round(dolares, 2) #Tomamos el contenido de la variable dolar y lo reducimos a dos decimales 
    dolares = str(dolares)  #Convertimos el valor de dolares a texto o string
    print(" Tienes $" + dolares + " dolares ")


menu = """ Bienvenidos al conversor de monedas 

        1-Pesos colombianos
        2-Pesos argentinos
        3-Pesos mexicanos

        Elija una opcion : """

opcion = int(input(menu))

if opcion == 1:
    conversor("colombianos", 3875)

elif opcion ==2:
    conversor("argentinos", 65)

elif opcion ==3:
    conversor("mexicanos", 24)

else:
    print("Ingresa una opcion correcta ")
    


