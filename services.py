import grafo
import no

def arvore_geradora_minima_prim(graph):
    arv_minima = grafo.Grafo()
    corte = grafo.Grafo()
    corte.addVertice(graph.vertices[0])

    while not verifica_arv_minima(graph, arv_minima):


def seleciona_menor_aresta(graph):
    menor_peso = float('inf')
    
    for vertice in graph.vertices:
        for aresta in vertice.adjacentes:
            if (graph.getVertice(aresta.vertice) == None):
                if (aresta.peso < menor_peso):
                    menor_peso = aresta
    return menor_peso

def verifica_arv_minima(graph, arv):
    lista_vertices_grafo = get_all_vertices(graph)
    lista_vertices_arv = get_all_vertices(arv)

    for vertice in lista_vertices_grafo:
        if vertice not in lista_vertices_arv:
            return False
    return True

def get_all_vertices(graph):
    lista_vertices = list()
    for v in graph.vertices:
        lista_vertices.append(v.vertice)
    return lista_vertices
        
