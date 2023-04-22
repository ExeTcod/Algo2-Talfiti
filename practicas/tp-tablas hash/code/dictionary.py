from ast import Interactive
from algo1 import *
from LibreriaExe import *
from LinkedList import *


class dictionaryNode:
  value = None
  key = None
  nextNode = None


class dictionary:
  head = None


#Dictionary = Array(m,0)
D = Array(m, 0)


#Siempre elegir un numero primo para las funcones hash
def h(k, m):
  k % m


#Insert-metodo encadenamiento
def insert(D, key, value):
  hash = h(key)
  add(D[hash], value)
  return D


#Search-metodo encadenamiento
def search(D, key):
  hash = h(key)
  k = search(D[hash], key)
  return k


#Delete-metodo encadenamiento
def delete(D, key, value):
  hash = h(key)
  current = list.searchCurrent(D[hash], key)
  current.value = None
  delete(D[hash], value)
  #como hacer para igualar a none la key eliminada?
  return D
