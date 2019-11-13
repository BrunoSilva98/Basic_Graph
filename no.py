from copy import deepcopy
class No:
    def __init__(self, vertice):
        self.vertice = vertice
        self.adjacentes = list()
    
    def copy(self):
        return deepcopy(self)