import pydot
from IPython.display import Image, display
import queue
import numpy as np


class Node ():
  def __init__(self, state,value,operators,operator=None, parent=None,objective=None):
    self.state= state
    self.value = value
    self.children = []
    self.parent=parent
    self.operator=operator
    self.objective=objective
    self.level=0
    self.operators=operators
    self.v=0


  def add_child(self, value, state, operator):
    node=type(self)(value=value, state=state, operator=operator,parent=self,operators=self.operators)
    node.level=node.parent.level+1
    self.children.append(node)
    return node

  def add_node_child(self, node):
    node.level=node.parent.level+1
    self.children.append(node)
    return node

  #Devuelve todos los estados según los operadores aplicados
  def getchildrens(self):
    return [
        self.getState(i)
          if not self.repeatStatePath(self.getState(i))
            else None for i, op in enumerate(self.operators)]

  def getState(self, index):
    pass

  def __eq__(self, other):
    return self.state == other.state

  def __lt__(self, other):
    return self.f() < other.f()


  def repeatStatePath(self, state):
      n=self
      while n is not None and n.state!=state:
          n=n.parent
      return n is not None

  def pathObjective(self):
      n=self
      result=[]
      while n is not None:
          result.append(n)
          n=n.parent
      return result

  def heuristic(self):
    return 0

  def cost(self):
    return 1

  def f(self):
    return self.cost()+self.heuristic()

  ### Crear método para criterio objetivo
  ### Por defecto vamos a poner que sea igual al estado objetivo, para cada caso se puede sobreescribir la función
  def isObjective(self):
    return (self.state==self.objetive.state)



class Tree ():
  def __init__(self, root ,operators):
    self.root=root
    self.operators=operators

  ## Método para dibujar el árbol
  def draw(self,path):
    graph = pydot.Dot(graph_type='graph')
    nodeGraph=pydot.Node(str(self.root.state)+"-"+str(0),
                          label=str(self.root.state),shape ="circle",
                          style="filled", fillcolor="red")
    graph.add_node(nodeGraph)
    path.pop()
    return self.drawTreeRec(self.root,nodeGraph,graph,0,path.pop(),path)

  ## Método recursivo para dibujar el árbol
  def drawTreeRec(self,r,rootGraph,graph,i,topPath,path):
    if r is not None:
      children=r.children
      for j,child in enumerate(children):
        i=i+1
        color="white"
        if topPath.value==child.value:
          if len(path)>0:topPath=path.pop()
          color='red'
        c=pydot.Node(child.value,label=str(child.state)+r"\n"+r"\n"+"f="+str(child.heuristic())+r"\n"+str(child.v),
                      shape ="circle", style="filled",
                      fillcolor=color)
        graph.add_node(c)
        graph.add_edge(pydot.Edge(rootGraph, c,
                                  label=str(child.operator)+'('+str(child.cost())+')'))
        graph=self.drawTreeRec(child,c,graph,i,topPath,path)  # recursive call
      return graph
    else:
      return graph

  def printPath(self,n):
    stack=n.pathObjective()
    path=stack.copy()
    while len(stack)!=0:
        node=stack.pop()
        if node.operator is not None:
            operator_selected = self.operators[node.operator]
            
    return path, operator_selected

  def reinitRoot(self):
    self.root.operator=None
    self.root.parent=None
    self.root.objective=None
    self.root.children = []
    self.root.level=0

  def miniMax(self, depth):
    self.root.v=self.miniMaxR(self.root, depth, True)
    ## Comparar los hijos de root
    values=[c.v for c in self.root.children]
    maxvalue=max(values)
    index=values.index(maxvalue)
    return self.root.children[index]

  def miniMaxR(self, node, depth, maxPlayer):
    # Condicion de parada
    if depth==0 or node.isObjective():
      node.v=node.heuristic()
      return node.heuristic()
    ## Generar los hijos del nodo
    children=node.getchildrens()

    ## Según el jugador que sea en el árbol
    if maxPlayer:
      value=float('-inf')
      for i,child in enumerate(children):
        if child is not None:
          newChild=type(self.root)(value=node.value+'-'+str(i),state=child,operator=i,parent=node,
                                   operators=node.operators,player=False)
          newChild=node.add_node_child(newChild)
          value=max(value,self.miniMaxR(newChild,depth-1,False))
      node.v=value
      return value
    else:
      value=float('inf')
      for i,child in enumerate(children):
        if child is not None:
          newChild=type(self.root)(value=node.value+'-'+str(i),state=child,operator=i,parent=node,
                                   operators=node.operators,player=True)
          newChild=node.add_node_child(newChild)
          value=min(value,self.miniMaxR(newChild,depth-1,True))
    node.v=value
    return value
  
  def alfaYbeta(self, depth):
      self.root.v = self.alfaYbetaR(self.root, depth, True, float('-inf'), float('inf'))
      # Comparar los hijos de root
      values = [c.v for c in self.root.children]
      maxvalue = max(values)
      index = values.index(maxvalue)
      return self.root.children[index]

  def alfaYbetaR(self, node, depth, maxPlayer, alpha, beta):
      # Condición de parada
      if depth == 0 or node.isObjective():
          node.v = node.heuristic()
          return node.heuristic()

      # Generar los hijos del nodo
      children = node.getchildrens()

      # Según el jugador que sea en el árbol
      if maxPlayer:
          value = float('-inf')
          for i, child in enumerate(children):
              if child is not None:
                  newChild = type(self.root)(value=node.value+'-'+str(i), state=child, operator=i, parent=node,
                                            operators=node.operators, player=False)
                  newChild = node.add_node_child(newChild)
                  value = max(value, self.alfaYbetaR(newChild, depth-1, False, alpha, beta))
                  alpha = max(alpha, value)
                  if alpha >= beta:
                      break
          node.v = value
          return value
      else:
          value = float('inf')
          for i, child in enumerate(children):
              if child is not None:
                  newChild = type(self.root)(value=node.value+'-'+str(i), state=child, operator=i, parent=node,
                                            operators=node.operators, player=True)
                  newChild = node.add_node_child(newChild)
                  value = min(value, self.alfaYbetaR(newChild, depth-1, True, alpha, beta))
                  beta = min(beta, value)
                  if alpha >= beta:
                      break
          node.v = value
          return value

class NodeNim(Node):

  def __init__(self, player=True,**kwargs):
    super(NodeNim, self).__init__(**kwargs)
    self.player=player


    if player:
      self.v=float('-inf')
    else:
      self.v=float('inf')


  def getState(self, index):
    state = self.state
    nextState = None
    # Obtiene los valores de la fila y la cantidad de palillos a remover
    (fila, cantidad_palillos) = self.operators[index]
    # Verifica si la longitud de la fila es mayor que la cantidad de palillos a remover
    if len(state[fila]) >= cantidad_palillos:
        nextState = [f.copy() for f in state]
        # Remueve la cantidad de palillos de la fila
        nextState[fila] = state[fila][:-cantidad_palillos]
    return nextState

  #Costo acumulativo(valor 1 en cada nivel)
  def cost(self):
    return self.level

  # Verifica si se han removido todos los palillos
  def isObjective(self):
    return all([len(f)==0 for f in self.state])

  def get_value_from_nim_sum(self, nim_sum):
        # En el juego de Nim Misere, queremos que el último que quite una pieza pierda.
        if not self.player:
            # Si el nim_sum es 0 y es el turno del jugador actual, queremos que esto sea desfavorable para ellos.
            return 1 if nim_sum == 0 else -1
        else:
            # Si el nim_sum es 0 y es el turno del oponente, es favorable para el jugador actual.
            return -1 if nim_sum == 0 else 1

  def heuristic(self):
    # Inicializa contadores para filas con un solo palito y para filas con un número impar de palitos.
    single_stick_rows = 0 
    odd_rows = 0 
    
    # Obtiene el estado actual del juego, que es una lista de filas, donde cada fila contiene un número de palitos.
    state = self.state 
    
    # Inicializa la suma de Nim (nim_sum) a 0. Esta variable se utilizará para calcular el nim sum del estado actual.
    nim_sum = 0 
    
    # Recorre cada fila en el estado actual del juego.
    for fila in state:
        # Aplica la operación XOR entre nim_sum y la longitud de la fila actual (número de palitos en la fila).
        nim_sum ^= len(fila)
        
        # Si la fila tiene exactamente un palito, incrementa el contador single_stick_rows.
        if len(fila) == 1: 
            single_stick_rows += 1
        
        # Si la fila tiene un número impar de palitos, incrementa el contador odd_rows.
        if len(fila) % 2 != 0: 
            odd_rows += 1
    
    # Calcula un valor basado en el nim sum utilizando un método auxiliar (asumido como `get_value_from_nim_sum`).
    nim_sum_value = self.get_value_from_nim_sum(nim_sum)

    # Si hay más de una fila con un solo palito, incrementa el valor de nim_sum_value en 1.
    # Esto podría estar favoreciendo un estado en el que hay múltiples filas con un solo palito.
    if single_stick_rows > 1:
        nim_sum_value += 1  
    
    # Si hay un número impar de filas con un número impar de palitos, incrementa el valor de nim_sum_value en 1.
    # Este ajuste sugiere que un estado con un número impar de filas impares es más favorable.
    if odd_rows % 2 == 0:
        nim_sum_value += 1 

    # Devuelve el valor de nim_sum_value, que representa la heurística evaluada para el estado actual.
    return nim_sum_value
