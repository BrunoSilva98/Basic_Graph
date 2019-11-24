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
