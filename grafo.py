class No:
    def __init__(self, vertice):
        self.vertice = vertice
        self.adjacentes = list()


class Grafo:
    def __init__(self):
        self.vertices = list()

    def addVertice(self, no):
        for i in self.vertices:
            if(no.vertice == i.vertice):
                print("Vertice ja adicionado anteriormente")
                return False
        self.vertices.append(vertice)
        return True

    def getVertice(self, identificacao):
        for i in self.vertices:
            if(i.vertice == identificacao):
                return i
        return None

    def addAresta(self, identificacao, vertice):
        for i in self.vertices:
            if (i == identificacao):
                i.adjacentes.append(vertice)
                return True
        return False


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

            print("\nVertice 2:", end="")
            vertex2 = input()
            vertex2 = grafo.getVertice(vertex2)

            if(vertex == None or vertex2 == None):
                print("Um dos vertices nao pertencem ao grafo!")
                break











