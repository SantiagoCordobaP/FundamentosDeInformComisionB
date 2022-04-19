import re
def unidos_(string,palabra1,palabra2):
    return bool(re.search(palabra1 + "_" + palabra2, string))
print(unidos_("santi", "cordoba", "18"))
print(unidos_("santi_cordob", "cordoba", "18"))