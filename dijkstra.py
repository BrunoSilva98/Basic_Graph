class Dijsktra:

    def __init__(self, grafo, no_origem, no_destino):
        self.origem = no_origem
        self.destino = no_destino
        self.lista_distancia_acumulada = list()
        self.graph = grafo.copy()
        self.menor_caminho = list()
        self.vertices_expandidos = list()

    def inicializa_lista(self):
        for vertice in self.graph.vertices:
            vertice.distancia_acumulada = float('inf')
            vertice.anterior = None

            for adjacente in vertice.adjacentes:
                adjacente.distancia_acumulada = float('inf')
                adjacente.anterior = None

            if (vertice.vertice == self.origem.vertice):
                vertice.distancia_acumulada = 0

            self.lista_distancia_acumulada.append(vertice)
    
    def get_menor_vertice(self):
        menor_dist = float('inf')
        vertex = None
        for vertice in self.lista_distancia_acumulada:
            if (vertice.vertice not in self.vertices_expandidos):
                if (vertice.distancia_acumulada < menor_dist):
                    menor_dist = vertice.distancia_acumulada
                    vertex = vertice

        return vertex

    def atualiza_lista(self, anterior, atual, distancia_acumulada):
        atual.anterior = anterior
        atual.distancia_acumulada = distancia_acumulada

        for vertex in self.lista_distancia_acumulada:
            if(vertex.vertice == atual.vertice):
                vertex.anterior = anterior
                vertex.distancia_acumulada = distancia_acumulada
                break
    
    def get_adj_lista(self, vertice):
        for i in self.lista_distancia_acumulada:
            if i.vertice == vertice.vertice:
                i.peso = vertice.peso
                return i

    def dijsktra_algorithm(self):
        self.inicializa_lista()
        vertex = self.origem
        while(vertex.vertice != self.destino.vertice):
            vertex = self.get_menor_vertice()
            if(vertex != None):
                if(vertex.vertice != self.destino.vertice):
                    for adj in vertex.adjacentes:
                        adjacente = self.get_adj_lista(adj)
                        distancia_acumulada = vertex.distancia_acumulada + adjacente.peso

                        if(distancia_acumulada < adjacente.distancia_acumulada  and \
                            adjacente.vertice not in self.vertices_expandidos):
                            self.atualiza_lista(vertex, adjacente, distancia_acumulada)
                    self.vertices_expandidos.append(vertex.vertice)
            else:
                return False
        return True

    def preenche_lista_menor_caminho(self):
        caminho = None
        for vertex in self.lista_distancia_acumulada:
            if(vertex.vertice == self.destino.vertice):
                caminho = vertex
                break

        while caminho.vertice != self.origem.vertice:
            self.menor_caminho.insert(0, caminho)
            caminho = caminho.anterior

        self.menor_caminho.insert(0, caminho)

    def get_menor_vertice_adjacente(self, vertice, destino):
        menor_custo = float('inf')
        menor_aresta = None

        for vertex in vertice.adjacentes:
            if vertex.vertice == destino.vertice:
                if vertex.peso < menor_custo:
                    menor_custo = vertex.peso
                    menor_aresta = vertex
        return menor_aresta
   
    def printa_menor_caminho(self):
        self.preenche_lista_menor_caminho()
        contador = 0
        print("O menor caminho entre os dois vertices é:\n\n")

        while(contador < len(self.menor_caminho)):
            caminho = self.menor_caminho[contador]
            if caminho.vertice != self.destino.vertice:
                proximo = self.menor_caminho[contador+1]
                proximo = self.get_menor_vertice_adjacente(caminho, proximo)
                print("({0},{1}, peso {2})".format(caminho.vertice, proximo.vertice, proximo.peso))
            contador += 1

    
