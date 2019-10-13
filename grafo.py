class No:
    def __init__(self, vertice):
        self.vertice = vertice
        self.adjacentes = list()


class Grafo:
    def __init__(self):
        self.vertices = list()

    def addVertice(self, no):
        for i in self.vertices:
            if(i.vertice == no.vertice):
                print("Vertice ja adicionado anteriormente")
                return False
        self.vertices.append(vertice)
        return True

    def getVertice(self, no):
        for i in self.vertices:
            if(i.vertice == no):
                return i
        return None

    def addAresta(self, noOrig, noDest):
        for i in self.vertices:
            if (i.vertice == noOrig.vertice):
                i.adjacentes.append(noDest)
                return True
        return False
    
    def getAdjacentes(self, no):
        return no.adjacentes

    def mostrarAdjacentes(self, no):
        adjacentes = self.getAdjacentes(no)
        print("Vertices adjacentes ao no {0}".format(no.vertice))

        for i in range(adjacentes):
            print(adjacentes[i].vertice, end=", ")




if __name__ == '__main__':

    key = 0
    grafo = Grafo()

    while(key != 1):
        print("1. Sair")
        print("2. Inserir Vertice")
        print("3. Inserir Aresta")
        print("4. Representacao matematica")
        print("5. Visualizar vertices adjacentes")
        print("6. Verificar existencia de aresta")
        print("7. Calcular grau de um vertice")
        key = input()

        if(key == 2):
            print("Insira a identificacao do vertice")
            vertice = input()
            vertice = No(vertice)
            if(grafo.addVertice(vertice)):
                print("Vertice adicionado")
                break
        
        elif(key == 3):
            print("Vertice 1: ",end="")
            vertex = input()
            vertex = grafo.getVertice(vertex)

            print("\nVertice 2: ", end="")
            vertex2 = input()
            vertex2 = grafo.getVertice(vertex2)

            if(vertex != None and vertex2 != None): 
                #Por nao ser um grafo direcionado, a aresta deve estar nos dois vertices na lista
                grafo.addAresta(vertex, vertex2)
                grafo.addAresta(vertex2, vertex)
                break
            
            print("Um dos vertices nao pertencem ao grafo!")
            

        elif(key == 5):
            print("Insira o vertice do qual deseja visualizar os adjacentes: ", end="")
            no = input()
            no = grafo.getVertice(no)
            grafo.mostrarAdjacentes(no)

        











