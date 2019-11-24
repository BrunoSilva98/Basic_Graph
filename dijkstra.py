class Dijsktra:

    def __init__(self, grafo, no_origem, no_destino):
        self.origem = no_origem
        self.destino = no_destino
        self.lista_distancia_acumulada = list()
        self.graph = grafo.copy()
        self.menor_caminho = list()

    def inicializa_lista(self):
        for vertice in self.graph.vertices:
            vertice.distancia_acumulada = float('inf')
            vertice.expandido = False
            vertice.anterior = None

            if (vertice.vertice == self.origem.vertice):
                vertice.distancia_acumulada = 0

            self.lista_distancia_acumulada.append(vertice)
    
    def get_menor_vertice(self):
        menor_dist = float('inf')
        for vertice in self.lista_distancia_acumulada:
            if (vertice.expandido == False):
                if (vertice.distancia_acumulada < menor_dist):
                    menor_dist = vertice
        return menor_dist

    def atualiza_lista(self, anterior, atual, distancia_acumulada):
        for vertex in self.lista_distancia_acumulada:
            if(vertex.vertice == atual.vertice):
                atual.anterior = anterior
                atual.distancia_acumulada = distancia_acumulada

    def dijsktra_algorithm(self):
        self.inicializa_lista()
        vertex = self.origem
        while(vertex.vertice != self.destino.vertice):
            vertex = self.get_menor_vertice()
            for adjacente in vertex.adjacentes:
                distancia_acumulada = vertex.distancia_acumulada + adjacente.peso
                if(distancia_acumulada < adjacente.distancia_acumulada):
                    self.atualiza_lista(vertex, adjacente, distancia_acumulada)
            vertex.expandido = True

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

    def printa_menor_caminho(self):
        contador = 0
        print("O menor caminho entre os dois vertices é:\n\n")

        while(contador < len(self.menor_caminho)):
            caminho = self.menor_caminho[contador]
            if(caminho.vertice != self.destino.vertice):
                proximo = self.menor_caminho[contador+1]

                for vertex in caminho.adjacentes:
                    if (vertex.vertice == proximo.vertice and vertex.peso == proximo.peso):
                        proximo = vertex
                        break
                print("({0},{1}, peso {2})".format(caminho.vertice, proximo.vertice, proximo.peso))
            