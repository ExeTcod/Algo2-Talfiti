from algo1 import *


class LinkedList:
    head = None


class Node:
    value = None
    nextNode = None


#Función Add-Complejidad O(1)
def add(L, element):
    node = Node()
    node.value = element
    current = L.head
    if current == None:
        L.head = node
    else:
        node.nextNode = current
        L.head = node


#Funcion Search-Complejidad O(n)
def search(L, element):
    current = L.head
    currentpos = 0
    while current != None:
        if current.value == element:
            return currentpos
            break
        current = current.nextNode
        currentpos = currentpos + 1


def searchCurrent(L, element):
    current = L.head
    while current != None:
        if current.value == element:
            return current
            break
        current = current.nextNode


#Funcion Insert-Complejidad O(n)
def insert(L, element, position):
    current = L.head
    currentpos = 0
    newNode = Node()
    newNode.value = element
    if position == 0:
        add(L, element)
        return position
    else:
        while current != None:
            if currentpos == position - 1:
                newNode.nextNode = current.nextNode
                current.nextNode = newNode
                return position
                break
            else:
                current = current.nextNode
                currentpos = currentpos + 1


#Funcion Delete-Complejidad O(n)
def delete(L, element):
    current = L.head
    pos = search(L, element)
    if pos != None:
        if pos == 0:
            L.head = current.nextNode
            current = L.head
        else:
            for i in range(0, pos - 1):
                current = current.nextNode
            if current.nextNode != None:
                current.nextNode = current.nextNode.nextNode
            else:
                current.nextNode = None
        return pos
    else:
        return None


#Funcion Length-Complejidad O(n)
def length(L):
    current = L.head
    len = 0
    while current != None:
        current = current.nextNode
        len = len + 1
    return len


#Funcion Access-Complejidad O(n)
def access(L, position):
    current = L.head
    currentpos = 0
    if position > 0:
        while current != None and currentpos < position:
            current = current.nextNode
            currentpos = currentpos + 1
        if current != None:
            return (current.value)
        else:
            return (None)
    elif position == 0:
        return (current.value)


def accessCurrent(L, position):
    current = L.head
    currentpos = 0
    if position > 0:
        while current != None and currentpos < position:
            current = current.nextNode
            currentpos = currentpos + 1
        if current != None:
            return (current)
        else:
            return (None)
    elif position == 0:
        return (current)


#Funcion Update-Complejidad O(n)
def update(L, element, position):
    current = L.head
    Long = length(L)
    if position <= Long:
        currentpos = 0
        while current != None:
            if currentpos == position:
                current.value = element
                return position
                break
            else:
                current = current.nextNode
                currentpos = currentpos + 1
    else:
        return None