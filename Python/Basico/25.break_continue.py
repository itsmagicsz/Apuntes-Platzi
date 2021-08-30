def run():

    #CONTINUE
    #for contador in range(1000):
    #   if contador % 2 != 0:
    #      continue / si se cumple la condicion A partir de continue no se va a ejecutar lo que sigue
    #                  y pasamos a la otra vuelta del ciclo
    #  print(contador)
    
    #for i in range(10000):
    #    print(i)
    #    if i ==5678:
    #        break

    texto = input("Escribe un texto ")
    for letra in texto:
        if letra == "o":
            break
        print(letra)

if __name__ == '__main__':
    run()