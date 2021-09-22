# Reto : Utilice las palabras clave try, except y raise para elevar un error si el usuario ingresa 
# un numero negativo en nuestro programa de divisores

def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run ():
    try:
        num = int(input("Ingresa un numero: "))
        if num < 0 :
            raise ValueError("No se puede ingresar numeros negativos")
        print(divisors(num))
        print("Termino mi progrma")

    except ValueError as e :
        print(e)

if __name__ == "__main__":
    run()