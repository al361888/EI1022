from sesion1y2.labyrinthviewer import LabyrinthViewer
from sesion1y2.problema1 import create_labyrinth

def recorredor_aristas_profundidad(grafo, v_inicial):
    def recorrido_desde(u,v):
        seen.add(v)
        aristas.append((u,v))
        for suc in grafo.succs(v):
            if suc not in seen:
                recorrido_desde(v,suc)

    aristas = []

    seen = set()
    recorrido_desde(v_inicial,v_inicial)
    return aristas

def path(g, source, target):
    #Paso 1: obtener aristas(profundidad)
    la = recorredor_aristas_profundidad(g,source)

    #Paso 2: crear diccionario con el padre de cada vertice
    padre = {}
    for (u, v) in la:
        padre[v] = u

    #paso 3: recuperar camino desde target hasta source
    p=[]
    v = target
    p.append(v)
    while padre[v]!=v:
        v = padre[v]
        p.append(v)

    #Paso extra: darle la vuelta a p
    p2=p[::-1]

    #Paso 4
    return p2


if __name__ == '__main__':
    rows = 10
    cols = 20
    lab = create_labyrinth(rows, cols)
    source = (0,0)
    target = (rows - 1, cols - 1)
    camino = path(lab, source, target)

    viewer = LabyrinthViewer(lab, canvas_width=600, canvas_height=400, margin=10)
    viewer.add_path(camino, color='red')
    viewer.run()
