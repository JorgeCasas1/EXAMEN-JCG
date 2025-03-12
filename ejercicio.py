def buscarPalabra(objetivo, palabras):
    for palabra in palabras:
        if palabra == objetivo:
            return True
    return False
        

nombres = ["Perantano", "Zutano", "Fulano", "Mengano"]

palabras = {
    "Perantano": 0,
    "Zutano": 0,
    "Fulano": 0,
    "Mengano": 0 
}

def imprimirListaInversa(lista):
    resultado = []
    for i in range(len(lista)-1,-1,-1):
        resultado+= lista[i]
## ATAJO return lista [::-1]
print(imprimirListaInversa)

while True:
    nombre = input("Buscar nombre: ")
    if buscarPalabra(nombre, nombres):
        print("Mengano tiene 50 años")
    if nombre == "exit":
        break

print("FIN DEL PROGRAMA")
    

