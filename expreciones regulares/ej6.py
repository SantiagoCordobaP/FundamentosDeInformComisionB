import re
def lista_en_frase(lista,frase):
    return bool(re.search(lista in frase))

lista11 = ["hola", "que tal", "adios"]
print(lista_en_frase(lista11, "hola, que tal, adios"))

##esta mal##