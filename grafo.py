from no import No
class Grafo:
    def __init__(self):
        self.vertices = list()

    def addVertice(self, no):
        for i in self.vertices:
            if(i.vertice == no.vertice):
                return False
        self.vertices.append(no)
        return True

    def getVertice(self, no):
        for i in self.vertices:
            if(i.vertice == no):
                return i
        return None

    def mostrarVertices(self):
        for i in range(len(self.vertices)):
            print(self.vertices[i].vertice, end="")
            if(i+1 < len(self.vertices)):
                print(",", end= " ")

    def addAresta(self, noOrig, noDest):
        for i in self.vertices:
            if (i.vertice == noOrig.vertice):
                i.adjacentes.append(noDest)
                return True
        return False

    def contaLoops(self, vertice,adjacentes): #Criado para corrigir o print dos loops
        contador = 0
        for i in adjacentes:
            if i.vertice == vertice.vertice:
                contador += 1

        return contador/2


    def getArestas(self):
        listaMostrados = list()
        listaArestas = list()
        
        for i in self.vertices:
            loops = 0
            adjacentes = self.getAdjacentes(i)
            contador = self.contaLoops(i, adjacentes)
            
            while loops < contador:
                listaArestas.append([i.vertice, i.vertice])
                loops += 1
            listaMostrados.append(i.vertice)

            for j in adjacentes:
               if j.vertice not in listaMostrados:
                   listaArestas.append([i.vertice, j.vertice])

        return listaArestas
    
    def verificaAresta(self, noOrig, noDest):
        adjacentes = self.getAdjacentes(noOrig)
        for i in adjacentes:
            if (i.vertice == noDest.vertice):
                return True
        return False 
    
    def mostrarArestas(self):
        arestas = self.getArestas()
        
        for i in range(len(arestas)):
            print("({0},{1})".format(arestas[i][0], arestas[i][1]), end="")
            if (i+1 != len(arestas)):
                print(",", end=" ")

    def getAdjacentes(self, no):
        return no.adjacentes

    def getUniqueAdjacentes(self, no):
        adjacentes = self.getAdjacentes(no)
        listaMostrados = list()
        listaUnicos = list()

        for i in range(len(adjacentes)):
            if(adjacentes[i].vertice not in listaMostrados):
                listaMostrados.append(adjacentes[i].vertice)
                listaUnicos.append(adjacentes[i].vertice)
        return listaUnicos

    def mostrarAdjacentes(self, no):
        listaAdjacentes = self.getUniqueAdjacentes(no)
        for i in range(len(listaAdjacentes)):
            print("{0}".format(listaAdjacentes[i]), end="")
            if(i+1 != len(listaAdjacentes)):
                print(", ", end="")
        
    def calculaGrau(self, no):
        return len(self.getAdjacentes(no))

    def RepresentacaoMatematica(self):
        print("V(G) = {",end="")
        self.mostrarVertices()
        print("}")

        print("E(G) = {", end="")
        self.mostrarArestas()
        print("} - Grafo não direcionado")