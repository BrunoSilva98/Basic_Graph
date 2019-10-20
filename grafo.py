import os

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

if __name__ == '__main__':

    key = 0
    grafo = Grafo()

    while(key != '8'):
        print("1. Inserir Vertice")
        print("2. Inserir Aresta")
        print("3. Representacao matematica")
        print("4. Visualizar vertices adjacentes")
        print("5. Verificar existencia de aresta")
        print("6. Calcular grau de um vertice")
        print("7. Sair")

        key = input()
        os.system('cls||clear')

        if(key == '1'): #Insercao de vertices
            print("Insira a identificacao do vertice")
            vertex = input()
            vertex = No(vertex)
            if(grafo.addVertice(vertex)):
                print("Vertice adicionado")
            else:
                print("Vertice ja adicionado anteriormente")
            input()

        elif(key == '2'): #Insercao de arestas
            print("Vertice 1: ",end="")
            vertex = input()
            vertex = grafo.getVertice(vertex)

            print("\nVertice 2: ", end="")
            vertex2 = input()
            vertex2 = grafo.getVertice(vertex2)

            if(vertex != None and vertex2 != None): 
                #Por nao ser um grafo direcionado, a aresta deve estar nos dois vertices na lista
                if(grafo.addAresta(vertex, vertex2) and grafo.addAresta(vertex2, vertex)):
                    print("Aresta adicionada!")
            else:
                    print("Um dos vertices nao pertencem ao grafo!")
            input()

        elif(key == '3'): #Representacao matematica
            grafo.RepresentacaoMatematica()
            input()

        elif(key == '4'): #Visualizacao dos adjacentes de determinado vertice
            print("Insira o vertice do qual deseja visualizar os adjacentes: ", end="")
            vertex = input()
            vertex = grafo.getVertice(vertex)
            if(vertex != None):
                grafo.mostrarAdjacentes(vertex)
            else:
                print("Vertice nao pertencente ao grafo")
            input()

        elif(key == '5'): #Verificar existencia de aresta
            print("Vertice 1: ", end="")
            vertex = input()
            print("Vertice 2: ", end="")
            vertex2 = input()

            vertex = grafo.getVertice(vertex)
            vertex2 = grafo.getVertice(vertex2)

            if(vertex != None and vertex2 != None):
                if (grafo.verificaAresta(vertex, vertex2)):
                    print("Aresta {0}{1} existente".format(vertex.vertice, vertex2.vertice))
                else:
                    print("Nao existem arestas entre os vertices {0} e {1}".format(vertex.vertice, vertex2.vertice))
            else:
                print("Um dos vertices inseridos nao pertencem ao grafo")
            input()

        elif(key == '6'): #Calcular grau de um vertice
            print("Insira o vertice que deseja calcular o grau: ", end="")
            vertex = input()
            vertex = grafo.getVertice(vertex)
            
            if(vertex != None):
                grau = grafo.calculaGrau(vertex)
                print("\nGrau do vertice {0}: {1}".format(vertex.vertice, grau), end="")
            else:
                print("\n Vertice nao pertencente ao grafo!\n")
            input()

        elif(key == '7'):
            break
        
        os.system('cls||clear')