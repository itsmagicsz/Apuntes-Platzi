menu = """ Bienvenidos al conversor de monedas 

        1-Pesos colombianos
        2-Pesos argentinos
        3-Pesos mexicanos

        Elija una opcion : """

opcion = int(input(menu))

if opcion == 1:
    pesos = input("How many Colombian pesos do you have? ")
    pesos = float(pesos)
    valor_dolar = 3875
    dolares= pesos / valor_dolar
    dolares = round(dolares, 2) #Tomamos el contenido de la variable dolar y lo reducimos a dos decimales 
    dolares = str(dolares)  #Convertimos el valor de dolares a texto o string
    print(" Tienes $" + dolares + " dolares ")

elif opcion ==2:
    pesos = input("How many Argentine pesos do you have? ")
    pesos = float(pesos)
    valor_dolar = 65
    dolares= pesos / valor_dolar
    dolares = round(dolares, 2) #Tomamos el contenido de la variable dolar y lo reducimos a dos decimales 
    dolares = str(dolares)  #Convertimos el valor de dolares a texto o string
    print(" Tienes $" + dolares + " dolares ")

elif opcion ==3:
    pesos = input("How many mexican pesos do you have? ")
    pesos = float(pesos)
    valor_dolar = 24
    dolares= pesos / valor_dolar
    dolares = round(dolares, 2) #Tomamos el contenido de la variable dolar y lo reducimos a dos decimales 
    dolares = str(dolares)  #Convertimos el valor de dolares a texto o string
    print(" Tienes $" + dolares + " dolares ")

else:
    print("Ingresa una opcion correcta ")
    


