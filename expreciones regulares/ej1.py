import re
def caracteres_permitidos(palabra):
    return bool(re.search("[a-zA-Z0-9.]", palabra))

print(caracteres_permitidos('///'))
print(caracteres_permitidos('sant1'))