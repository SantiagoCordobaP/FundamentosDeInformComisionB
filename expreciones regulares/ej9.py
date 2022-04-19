import re
def entre_guiones(string):
    return (re.findall("-,-", string))

print (entre_guiones ("la paciencia es la virtud de la -ciencia-"))

