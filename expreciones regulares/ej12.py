sustituir = [" ", "_", ":"]
import re
def reemplazar(string):
    return re.sub(sustituir,"|",string)

print(reemplazar("hola como va"))


