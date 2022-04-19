#ejercicio5
def susti (arch1,arch2):
    with open(arch1, "r") as f, open (arch2,"w") as a:
        for palabra in f.read():
            for letra in palabra:
                a.write(letra.replace(letra,letra + "\n"))