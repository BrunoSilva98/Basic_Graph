import grafo

def arvore_geradora_minima_prim(graph):
    arv_minima = grafo.Grafo()
    corte = grafo.Grafo()
    #Definindo ponto inicial de onde será realizado algoritmo de prim
    vertice_inicial = graph.vertices[0].copy()
    corte.addVertice(vertice_inicial.copy()) #Adicionado no corte o vertice e todas suas arestas
   
    vertice_inicial.adjacentes.clear()
    arv_minima.addVertice(vertice_inicial) #Adicionado na arvore minima somente o vertice
    
    while not verifica_arv_minima(graph, arv_minima):
        aresta = seleciona_menor_aresta(corte)   
        peso = aresta[1].peso 
        corte.addVertice(graph.getVertice(aresta[1].vertice).copy())  #Adicionado no corte o vertice onde estava a aresta minima
        
        aresta[0].adjacentes.clear()
        aresta[1].adjacentes.clear()
        arv_minima.addVertice(aresta[1]) #Adicionado na arvore somente o vertice da aresta minima
        #Adicionando somente a aresta minima nos respectivos vertices
        vertex1 = arv_minima.getVertice(aresta[0].vertice)
        vertex2 = arv_minima.getVertice(aresta[1].vertice)
        vertex1.peso = peso
        vertex2.peso = peso
        arv_minima.addAresta(vertex1, vertex2.copy())
        arv_minima.addAresta(vertex2, vertex1.copy())
    
    return arv_minima

def seleciona_menor_aresta(graph):
    menor_peso = float('inf')
    vertex = None
    for vertice in graph.vertices:
        for aresta in vertice.adjacentes:
            if (graph.getVertice(aresta.vertice) == None):
                if (aresta.peso < menor_peso):
                    vertex = vertice.copy()
                    menor_peso = aresta.peso
                    edge = aresta.copy()
    return [vertex, edge]

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
        
