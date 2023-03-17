class BinaryTree:
    root = None

class BinaryTreeNode:
    key = None
    value = None
    leftnode = None
    rightnode = None
    parent = None

from LinkedList import *
from LibreriaExe import *

def search(B, element):
    node = searchNodeR(B.root, element)
    if node == None: return
    else: return node.key
def searchNodeR(node, element):
    if node == None: return
    if node.value == element:
        return node
    right = searchNodeR(node.rightnode, element)
    if right != None:
        return right
    left = searchNodeR(node.leftnode, element)
    if left != None:
        return left
def searchNode(B, element):
    return searchNodeR(B.root, element)
def insert(B, element, key):
    newNode = BinaryTreeNode()
    newNode.key = key
    newNode.value = element
    if (B.root == None):
        B.root = newNode
        return key
    return insertR(newNode, B.root)
# Función recursiva de insert
def insertR(newNode, currentNode):
    if newNode.key > currentNode.key:
        if currentNode.rightnode == None:
            newNode.parent = currentNode
            currentNode.rightnode = newNode
            return newNode.key
        else:
            right = insertR(newNode, currentNode.rightnode)
            if right != None:
                return right
    else:
        if currentNode.leftnode == None:
            newNode.parent = currentNode
            currentNode.leftnode = newNode
            return newNode.key
        else:
            left = insertR(newNode, currentNode.leftnode)
            if left != None:
                return left
def delete(B, element):
    node = searchNode(B, element)
    if node == None: return
    else: return deleteCurrentCase(B, node)
# Valida y ejecuta los distintos casos de delete
def deleteCurrentCase(B, node):
    if node.rightnode == None:
        if node.leftnode == None:
            # Caso 1: El nodo a eliminar es una hoja
            if node.parent.leftnode != None and node.parent.leftnode == node:
                node.parent.leftnode = None
                return node.key
            elif node.parent.rightnode != None and node.parent.rightnode == node:
                node.parent.rightnode = None
                return node.key
        # Caso 2: El nodo a eliminar tiene un hijo del lado izquierdo
        if node.parent.leftnode != None and node.parent.leftnode == node:
            node.parent.leftnode = node.leftnode
            return node.key
        elif node.parent.rightnode != None and node.parent.rightnode == node:
            node.parent.rightnode = node.leftnode
            return node.key
    else:
        # Caso 2: El nodo a eliminar tiene un hijo del lado derecho
        if node.leftnode == None:
            if node.parent.leftnode == node:
                node.parent.leftnode = node.rightnode
                return node.key
            elif node.parent.rightnode == node:
                node.parent.rightnode = node.rightnode
                return node.key
        else:
            # Caso 3: El nodo a eliminar tiene dos hijos
            changeNode = smallerOf(node.rightnode)
            node.value = changeNode.value
            oldKey = node.key
            node.key = changeNode.key
            if changeNode.parent.leftnode == changeNode:
                changeNode.parent.leftnode = None
            elif changeNode.parent.rightnode == changeNode:
                changeNode.parent.rightnode = None
            return oldKey
            # o eliminar el mayor de sus menores
            changeNode = bigger(node.leftnode)
            node.value = changeNode.value
            oldKey = node.key
            node.key = changeNode.key
            if changeNode.parent.leftnode == changeNode:
                changeNode.parent.leftnode = None
            elif changeNode.parent.rightnode == changeNode:
                changeNode.parent.rightnode = None
            return oldKey
# Devuelve el elemento con menor key desde un nodo dado
def smaller(node):
    if node.leftnode != None:
        current = smaller(node.leftnode)
        if current != None:
            return current
    else:
        return node
# Devuelve el elemento con mayor key desde un nodo dado
def bigger(node):
    if node.rightnode != None:
        current = bigger(node.rightnode)
        if current != None:
            return current
    else:
        return node
def smallerOf(node):
    if node.leftnode != None:
        changeNode = smallerOf(node.leftnode)
        if changeNode != None:
            return changeNode
    elif node.rightnode != None:
        changeNode = smallerOf(node.rightnode)
        if changeNode != None:
            return changeNode
    else:
        return node
def biggerOf(node):
    if node.rightnode != None:
        changeNode = biggerOf(node.rightnode)
        if changeNode != None:
            return changeNode
    elif node.leftnode != None:
        changeNode = biggerOf(node.leftnode)
        if changeNode != None:
            return changeNode
    else:
        return node





def deleteKey(B, key):
    node = searchKeyR(B.root, key)
    if node == None: return
    else: return deleteCurrentCase(B, node)
# Función recursiva de searchKey
def searchKeyR(node, key):
    if node == None: return
    if node.key == key:
        return node
    right = searchKeyR(node.rightnode, key)
    if right != None:
        return right
    left = searchKeyR(node.leftnode, key)
    if left != None:
        return left
def access(B, key):
    node = searchKeyR(B.root, key)
    if node == None: return
    else: return node.value
def update(B, element, key):
    node = searchKeyR(B.root, key)
    if node == None: return
    else:
        node.value = element
        return node.key
def traverseInOrder(B):
    L = LinkedList()
    traverseInOrderR(B.root, L)
    return revert(L)
# Función recursiva de traverseInOrder
def traverseInOrderR(node, L):
    if node != None:
        traverseInOrderR(node.leftnode, L)
        add(L, node.value)
        traverseInOrderR(node.rightnode, L)
def traverseInPostOrder(B):
    L = LinkedList()
    traverseInPostOrderR(B.root, L)
    return revert(L)
#Funcion recursiva de traverseInPostOrder
def traverseInPostOrderR(node, L):
    if node != None:
        traverseInPostOrderR(node.leftnode, L)
        traverseInPostOrderR(node.rightnode, L)
        add(L, node.value)
def traverseInPreOrder(B):
    L = LinkedList()
    traverseInPreOrderR(B.root, L)
    return revert(L)
# Función recursiva de traverseInPreOrder
def traverseInPreOrderR(node, L):
    if node != None:
        add(L, node.value)
        traverseInPreOrderR(node.leftnode, L)
        traverseInPreOrderR(node.rightnode, L)
from myqueue import enqueue, dequeue
def traverseBreadFirst(B):
    queue = LinkedList()
    valuesQueue = LinkedList()
    enqueue(queue, B.root)
    while queue.head != None:
        node = dequeue(queue)
        enqueue(valuesQueue, node.value)
        if node.leftnode != None:
            enqueue(queue, node.leftnode)
        if node.rightnode != None:
            enqueue(queue, node.rightnode)
    return revert(valuesQueue)

class AVLTree:
	root = None
class AVLNode:
  parent = None
  leftnode = None
  rightnode = None
  key = None
  value = None
  bf = None	
        


#Ejercicio1
def rotateLeft(Tree,avlnode):
	if avlnode.rightnode.leftnode==None:
    if avlnode==Tree.root:
      Tree.root=avlnode.rightnode
      avlnode.rightnode=None
    else:
      avlnode.rightnode.parent=avlnode.parent
      avlnode.parent=avlnode.rightnode
      avlnode.rightnode=None
  else:
    if avlnode==Tree.root:
      Tree.root=avlnode.rightnode
      avlnode.rightnode=avlnode.rightnode.leftnode
    else:
      avlnode.rightnode.parent=avlnode.parent
      avlnode.parent=avlnode.rightnode
      avlnode.rightnode=avlnode.rightnode.leftnode
def rotateright(Tree,avlnode):
	if avlnode.leftnode.rightnode==None:
    if avlnode==Tree.root:
      Tree.root=avlnode.leftnode
      avlnode.leftnode=None
    else:
      avlnode.leftnode.parent=avlnode.parent
      avlnode.parent=avlnode.leftnode
      avlnode.leftnode=None
  else:
    if avlnode==Tree.root:
      Tree.root=avlnode.leftnode
      avlnode.leftnode=avlnode.leftnode.rightnode
    else:
      avlnode.leftnode.parent=avlnode.parent
      avlnode.parent=avlnode.leftnode
      avlnode.leftnode=avlnode.leftnode.rightnode

#Ejercicio2
#En la siguiente funcion calculamos el balance factor de un nodo en especifico
def CalculateBFTree(AVLTree,avlnode): 
  SubTleft=0
  SubTright=0
  bf=0
  if avlnode.leftnode!=None:
    avlnode=avlnode.leftnode
    node=leftnode
    SubTleft=1
    while avlnode.leftnode!=None or avlnode.rightnode!=None:
      if  avlnode.leftnode.leftnode!=None or avl.leftnode.rightnode!=None:
        node=leftnode
      elif avlnode.rightnode.leftnode!=None or avl.rightnode.rightnode!=None:
        node=rightnode
      else:
        node=leftnode
      SubTleft+=1
      avlnode=avlnode.node
  
  if avlnode.rightnode!=None:
    avlnode=avlnode.rightnode
    node=rightnode
    SubTright=1
    while avlnode.leftnode!=None or avlnode.rightnode!=None:
      if  avlnode.rightnode.leftnode!=None or avl.rightnode.rightnode!=None:
        node=rightnode
      elif avlnode.leftnode.leftnode!=None or avl.leftnode.rightnode!=None:
        node=leftnode
      else:
        node=rightnode
      SubTright+=1
      avlnode=avlnode.node
  bf=SubTleft-SubTright
  return bf
  #En la siguiente funcion calculamos el balance factor de todos los  nodos.
  def calculateBalance(AVLTree):
    AVLTreeBalanced=AVLTree()
    avlnode=AVLTree.root
    AVLTreeBF=calculateBalanceR(AVLTree,avlnode)
    return AVLTreeBF
  def calculateBalanceR(AVLTree,avlnode)
    avlnode.bf=CalculateBFTree(AVLTree,avlnode)
    calculateBalanceR(AVLTree,avlnode.leftnode)
    calculateBalanceR(AVLTree,avlnode.rightnode)
    return AVLTree
#Ejercicio 3
#buscamos un nodo que tenga bf < a -1 o > a 1
def searchAVLBF(AVLTree):
    node = searchNodeR(B.root)
    if node == None: return
    else: return node.key


# Función recursiva de search 
def searchAVLBF_R(node):
    if node == None: return

    if node.bf < -1 or node.bf > 1 :
      return node

    right=searchNodeR(node.rightnode)
    if right != None:
      return right

    left = searchNodeR(node.leftnode)
    if left != None:
      return left

def reBalance(AVLTree):
  AVLTree=calculateBalance(AVLTree)
  avlnode=searchAVLBF(AVLTree)
  while avlnode!=None:
    if avlnode.bf < 0:
      if avlnode.rightnode.bf > 0:
        rotateRight(avlnode.rightnode)
        rotateLeft(avlnode)
      else:
        rotateLeft(avlnode)
    elif avlnode.bf > 0:
        if avlnode.leftnode.bf < 0:
          rotateLeft(avlnode.leftnode)
          rotateRight(avlnode)
        else:
          rotateRight(avlnode)
    AVLTree=calculateBalance(AVLTree)
    avlnode=searchAVLBF(AVLTree)
  return AVLTree
#Ejercicio 4
def InsertAVL(AVLTree, avlnode):
  insert(AVLTree, avlnode, avlnode.key)
  reBalance(AVLTree)
  return AVLTree
#Ejercicio 5
def DeleteAVL(AVLTree, avlnode):
  deleteKey(AVLTree, avlnode.key)
  reBalance(AVLTree)
  return AVLTree