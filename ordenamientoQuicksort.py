lista=[]
suma=0
contador=0
while True:
    num=int(input("ingrese el numero de 1 al 20: "))
    if num<1 or num>20:
        break


    lista.append(num)
    contador=contador+1
    suma=suma+num
print(lista)
prom=suma/len(lista)
print(prom)
lista.append(prom)
print(lista)

def quicksort(lista):
    if(len(lista) <= 1):
        return lista
    else:
        pivot = lista[0]
        menores = []
        mayores = []
    for i in range(1, len(lista)):
        if(lista[i] > pivot):
            mayores.append(lista[i])
        else:
            menores.append(lista[i])
    mayores = quicksort(mayores)
    menores = quicksort(menores)
    return menores + [pivot] + mayores
print(quicksort(lista))