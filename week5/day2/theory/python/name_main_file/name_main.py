"""
variable built-in __name__: 

1- Tiene el valor de "__main__" si se ejecuta ese fichero
2- Tiene el valor del nombre del fichero si se está importando

"""

#from a import x
import a
import numpy as np

print("a.__name__:", a.__name__)

#Code
#x()

print("-----------")
print("Ejecución de 'name&main'")

print("Valor de __name__:", __name__)

if __name__ == "__main__":
    print("name de 'name&main':")
    print(__name__)
    print("EQ")
print("Fin de ejecución de 'name&main'")
print("----------")

