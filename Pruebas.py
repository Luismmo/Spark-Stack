import os
import time
from graphviz import Digraph
""" #prueba congelamiento de tiempo
print("incio")
time.sleep(2)
print("dos segundos despues") """

""" a = "a A c"
li = a.split(" ")
print(li) """
""" f = Digraph(filename='ArbolDerivacion.dot', format='png', encoding='UTF-8')
f.attr(rankdir = 'TB')
f.edge_attr.update(arrowhead='none')
f.attr('node', shape='none')
f.node('0','A')
f.node('1','B')
f.edge('0','1')
f.node('2','C')
f.edge('0','2')
f.view() """
a = []
print("Tamaño: "+str(len(a)))
a.append(1)
a.append(2)
print(a)
print("Tamaño: "+str(len(a)))
a.remove(1)
a.remove(2)
print("Tamaño: "+str(len(a)))
a.append("d")
a.append("d")
print("Tamaño: "+str(len(a)))
print(a)