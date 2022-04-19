import re
def tiene_caracteres(string):
    return bool(re.findall("[a-zA-Z0-9.]", string))

print(tiene_caracteres('santi'))
print(tiene_caracteres('i%7'))