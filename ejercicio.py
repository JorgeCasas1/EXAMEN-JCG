def imprimirListaInversa(lista):
    resultado = []
    for i in range(len(lista)-1,-1,-1):
        resultado+= i


nombres =['Peratano','Zutano','Fulano','Mengano']  
print(imprimirListaInversa([nombres]))   

# Los -1 nos sirven para leer la list a la inversa


