"""Programa de metodos de ordenamiento"""

import random, sys, time

#Funcion  generar Vector
def NVector(n):
    #Verifica que el valor para generar el vector sea mayor a 0
    if n > 0: 
        #Genera el vector aleatoriamente entre 1000, 9999
        lista = [] # O(1)
        for i in range(0, n): # O(n)
            lista.append(random.randrange(1000,10000)) #O(1)
        return lista # O(1)
    else:
        print("¡No se puede crear un vector de tamaño negativo o 0!")
        sys.exit(True)

#Ordeamiento Burbuja
def OrdBurbuja(lista):
    #Se referncia las variables globales para sobreescribir
    global tiempo_inicio_burb, tiempo_final_burb
    #Se toma el tiempo al iniciar el algoritmo de ordenamento
    tiempo_inicio_burb = time.time()
    for i  in range(1,len(lista)):
        for j in range(0,len(lista)-+i):
            if lista[j+1]<lista[j]:
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
    #Se toma el tiempo una vez termino el algoritmo
    tiempo_final_burb = time.time()
    return lista 

#Ordenamiento Por Insercion
def OrdInserc(lista):
    global tiempo_inicio_Inser, tiempo_final_Inser
    tiempo_inicio_Inser = time.time()
    for i in range(len(lista)):
        for j in range(i,0,-1):
            if(lista[j-1] > lista[j]):
                aux=lista[j]
                lista[j]=lista[j-1]
                lista[j-1]=aux
    tiempo_final_Inser = time.time()
    return lista

#Ordenamiento QuickSort1
def OrdQuickSort(lista):
    
    if len(lista) <= 1:
        return lista
        
    derecha = []
    izquierda = []
    medio = []
    pivote = lista[0]
    medio.append(pivote)

    for i  in range(1,len(lista)):
        if lista[i] < pivote:
            izquierda.append(lista[i])
            
        else:
            derecha.append(lista[i])

    return OrdQuickSort(izquierda) + medio + OrdQuickSort(derecha)

#Busqueda Secuencial
def BusSecuen(lista, eval):
    n=0
    while n < len(lista):
        if eval == lista[n]:
            return n
        n += 1
    
    return -1

#Busqueda Binaria 
def BusBinaria(lista, eval):
    inf = 0
    sup = len(lista) - 1
    while inf <= sup:
        mit =  inf+sup//2
        if lista[mit] == eval:
            return mit
        elif eval < lista[mit]:
            sup = mit - 1
        else:
            inf = mit + 1
    
    return -1

#Metodo para Imprimir Resultado De Busqueda
def imprResultado(valor, elemento):
    if valor >= 0:
         print(F"El elemento: {elemento} se encuentra en la posicion {valor}")
    else:
         print(F"El elemento: {elemento} no se encuentra en la lista")
    
def main():
    #sys.setrecursionlimit(15000)
    print("Programa de  metodos de Ordenamiento y Busqueda")
    n =  int(input("Ingrese un tamaño para el vector: "))
    vec=NVector(n)
    print("Seleccione el metodo de ordenamiento o bsuqueda")
    o = int(input("1 - Burbuja \n2 - Inserción \n3 - Quick Sort \nselección : "))
        
    tiempo_inicio_burb  = 0
    tiempo_inicio_Inser = 0
    tiempo_inicio_Quick = 0
    tiempo_final_burb  = 0
    tiempo_final_Inser = 0
    tiempo_final_Quick = 0
    vecOrd = []

    if o == 1:
        print(f"Para un vector de tamaño {n}, el algoritmo de burbuja se demoro: {tiempo_final_burb-tiempo_inicio_burb} ")
    elif o == 2:
        print(f"Para un vector de tamaño {n}, el algoritmo de inserción se demoro: {tiempo_final_Inser-tiempo_inicio_Inser} ")
    elif o == 3:
        tiempo_inicio_Quick = time.time()
        vecOrd = OrdQuickSort(vec)
        tiempo_final_Quick =  time.time()
        print(f"Para un vector de tamaño {n}, el algoritmo QuickSort se demoro: {tiempo_final_Quick-tiempo_inicio_Quick} ")
    else : 
        print("Seleccion Incorrecta Selecciona 1, 2 o 3")
        sys.exit(True)

    print("Seleccione el tipo de busqueda para un elemento")
    b = int(input("1 - Busqueda Secuencial \n2 - Buesqueda Binaria \nselección : "))

    if b == 1:
        val = int(input("Ingresa el valor a buscar en el vector: "))
        imprResultado(BusSecuen(vecOrd, val), val)
    elif b == 2:
        val = int(input("Ingresa el valor a buscar en el vector: "))
        imprResultado(BusBinaria(vecOrd, val), val)
    else:
        print("Seleccion Incorrecta Selecciona 1 o 2")
        sys.exit(True)


if __name__ == "__main__":
    main()

