def read():
    numbers = []
    with open("./archivos/numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)

def write():
    names = ["facundo", "Miguel", "Pepe", "Charlie", "Roció"]
    with open("./archivos/names.txt", "w", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")

def run():
    write()

if __name__ == '__main__':
    run()

""" encoding="utf-8" -> Puede ser que cuando uno lea archivos haya un caracter extraño 
como una palabra con tildes o la ñ. entonces ese parametro (encoding="utf-8") nos aseguramos
que no tenga caracteres extraños u ocurran errores """