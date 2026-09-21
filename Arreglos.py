"""#Declarando un arreglo
numeros = [10, 20, 30, 40, 50,]

#Imprimo un elemento del especifico del arreglo
print(numeros[2])

#Reasignacion 
numeros[3] = 35
print(numeros[3])

#Agrega un nuevo valor al final del arreglo
numeros.append(60)
print(numeros)

#Eliminamos un numero definido
numeros.remove(35)
print(numeros)

#Eliminamos un valor del arreglo usando la posicion
numeros.pop(4)
print(numeros)

#Eliminamos un elemento del arreglo usando el numero
frutas = ["Manzana", "Fresa", "Sandia", "Mango", "Melon", "Platano"]
frutas.pop(4)
print(frutas)


frutas.remove("Manzana")
print(frutas)  


arreglo = []

print(arreglo)

n = int(input("INGRESE EL TAMANO DEL ARREGLO: "))

arreglo = [0] * n

for i in range(n):
    dato = int(input("INGRESE UN NUMERO: "))
    arreglo[i] = dato
 """


numeros = []

for i in range(15):
    while True:
        num = int(input(f"INGRESE UNOS VALORES {i + 1} (0-500): "))
        if 0 <= num <= 500:
            numeros.append(num)
            break
        else:
            print("INGRESE UN NUMERO ENTRE 1 AL 500")

print(numeros)

cincuentizar = []

for num in numeros:
    if num % 5 == 0:
        cincuentizar.append(num)
    else:
        sig = num + (5 - num % 5)
        cincuentizar.append(sig)

print(cincuentizar)


