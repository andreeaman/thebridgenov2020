import name_main

print("-----------")
print("Ejecución de 'a'")

def y():
    return 7

def x():
    print("__name__ de 'a':")
    print(__name__)
    print("Estoy en el archivo 'a'")
   
f = 2
 
print("Fin de ejecución de 'a'")
print("-----------")

if __name__ == "__main__":
    print("__name__ de a cumple condición")