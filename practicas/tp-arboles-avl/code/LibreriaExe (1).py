from algo1 import Array
from random import randint
from LinkedList import *


#funcion para imprimir matriz
def print_matriz(matriz):
    for i in matriz:
        print(i, end="  ")
        print()


fila = randint(0, 5)
columna = randint(0, 5)
matriz = Array(fila, Array(columna, 0))


#funcion para llenar matriz
def creando_matriz(matriz, fila, columna):
    for x in range(0, fila):
        for n in range(0, columna):
            matriz[x][n] = randint(0, 5)


#funcion para llenar matriz con elementos nulos
def creando_matriz_nula(matriz, fila, columna):
    for x in range(0, fila):
        for n in range(0, columna):
            matriz[x][n] = 0


#funcion para llenar vector
def llenar_vector(vector, dimension):
    for i in range(0, dimension):
        vector[i] = randint(0, 10)


#funcion que busca el mayor elemento de una matriz
def mayor_elemento(vector, dimension, mayor):
    for i in range(0, dimension):
        if vector[i] > mayor:
            mayor = vector[i]


#funcion para sacar modulo de un vector
def modulo_vector(vector_suma, dimension):
    sum_cuad = 0
    for x in range(0, dimension):
        sum_cuad = sum_cuad + pow(vector_suma[x], 2)
    mod = sqrt(sum_cuad)
    print("el modulo de su vector es:", mod)


def MTriangS(fila, colum, matriz):
    MTS = 0
    for i in range(0, fila):
        for j in range(0, colum):
            if i > j:
                if matriz[i][j] == 0:
                    MTS = MTS + 1
                else:
                    MTS = 0
                    break
    return MTS


def det_MTriang(fila, colum, matriz):
    determinante = 1
    for i in range(0, fila):
        for j in range(0, colum):
            if i == j:
                determinante = determinante * matriz[i][j]
    return determinante


#funcion para imprimir lista

#funcion para revertir una lista
def revert(L):
    new = LinkedList()
    len = length(L)
    current = L.head

    for i in range(len):
        len -= 1
        add(new, current.value)
        current = current.nextNode
    return new


#funcion para imprimir lista empleados
def print_list_emp(L):
    current = L.head
    currentPos = 0

    while current != None:
        if currentPos != 0: print(" | ")
        print(current.value.nombre, end=", ")
        print(current.value.edad, end=", ")
        print(current.value.nroLegajo)
        current = current.nextNode
        currentPos += 1
    print()
    return currentPos


#search en empleados
def searchEmp(L, nroLegajo):
    current = L.head
    currentPos = 0

    while current != None:
        if current.value.nroLegajo == nroLegajo:
            return currentPos

        current = current.nextNode
        currentPos += 1
    return



def print_list(L):
    current = L.head
    currentPos = 0

    while current != None:
        if currentPos != 0: print(end=" -> ")
        print(current.value, end="")
        current = current.nextNode
        currentPos += 1
    print()
    return currentPos


from random import randint


def random_list(length, rnd_from, rnd_to):
    L = LinkedList()
    for i in range(length):
        add(L, randint(rnd_from, rnd_to))
    return L


def moveNode(L, position_orig, position_dest):
    if position_orig == position_dest: return
    elif position_orig == 0:
        # La head es la posición de origen
        originalNode = L.head

        L.head = L.head.nextNode
        previousDest = previousNode(L, position_dest)

        originalNode.nextNode = previousDest.nextNode
        previousDest.nextNode = originalNode
    elif position_dest == 0:
        # La head es la posición de destino
        previousOrig = previousNode(L, position_orig)
        originalNode = previousOrig.nextNode

        if previousOrig.nextNode != None:
            previousOrig.nextNode = previousOrig.nextNode.nextNode
        else:
            previousOrig.nextNode = None

        originalNode.nextNode = L.head
        L.head = originalNode
    else:
        previousOrig = previousNode(L, position_orig)
        originalNode = previousOrig.nextNode

        if previousOrig.nextNode != None:
            previousOrig.nextNode = previousOrig.nextNode.nextNode
        else:
            previousOrig.nextNode = None

        previousDest = previousNode(L, position_dest)
        originalNode.nextNode = previousDest.nextNode
        previousDest.nextNode = originalNode


def previousNode(L, position):
    count = 0
    current = L.head
    while count < position - 1:
        current = current.nextNode
        count += 1
    return current


def swapNodes(list, nodeAPos, nodeBPos):
    nodeB = accessNode(list, nodeBPos)

    moveNode(list, nodeAPos, nodeBPos)
    nodeBnewPos = searchNode(list, nodeB)
    moveNode(list, nodeBnewPos, nodeAPos)
