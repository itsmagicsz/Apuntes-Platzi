def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run ():
        num = input("Ingresa un numero: ")
        assert num.isnumeric(), "Ingresa un numero no una letra "
        print(divisors(int(num)))
        print("Termino mi progrma")

if __name__ == "__main__":
    run()


"""Estructura:
 assert condicion, mensajde de error
 Le está diciendo al programa que pruebe esa condición y que de inmediato provoque un error si es falso. 
 y enviele cierto mensaje """