class Dijsktra:

    def __init__(self, grafo, no_origem, no_destino):
        self.origem = no_origem
        self.destino = no_destino
        self.lista_distancia_acumulada = list()
        self.graph = grafo.copy()

    def inicializa_lista(self):
        for vertice in self.graph.vertices:
            vertice.distancia_acumulada = float('inf')
            vertice.expandido = False
            vertice.anterior = None

            if (vertice.vertice == self.origem.vertice):
                vertice.distancia_acumulada = 0
    
    def dijsktra_algorithm(self):
        pass
