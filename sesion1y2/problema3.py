from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.mergefindsets import MergeFindSet
from sesion1y2.labyrinthviewer import LabyrinthViewer
import random

#Copia y pega del problema 1
def create_labyrinth(rows, cols): #Intentar Edges con expresion generatriz
    #Paso 1
    vertices = [(i,j) for i in range(rows) for j in range(cols)]
    #Paso 2
    mfs = MergeFindSet()
    for v in vertices:
        mfs.add(v)

    #Paso 3
    edges = []
    for r in range(rows):
        for c in range(cols):
            if r+1<rows:
                edges.append(((r,c),(r+1,c)))
            if c+1<cols:
                edges.append(((r,c),(r,c+1)))
    random.shuffle(edges)

    #Paso 4
    corridors = []

    #Paso 5
    for (u,v) in edges:
        if mfs.find(u) != mfs.find(v):
            mfs.merge(u,v)
            corridors.append((u,v))

    #Paso 6
    return UndirectedGraph(E=corridors)
