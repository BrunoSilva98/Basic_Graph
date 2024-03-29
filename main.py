from grafo import Grafo
from no import No
import os
import services
import dijkstra

if __name__ == '__main__':

    key = 0
    grafo = Grafo()

    while(key != '9'):
        print("1. Inserir Vertice")
        print("2. Inserir Aresta")
        print("3. Representacao matematica")
        print("4. Visualizar vertices adjacentes")
        print("5. Verificar existencia de aresta")
        print("6. Calcular grau de um vertice")
        print("7. Aplicar algoritmo de Prim para gerar Arvore minima")
        print("8. Aplicar algoritmo de Dijsktra")
        print("9. Sair")

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
                print("\nPeso da aresta: ", end="")
                
                try:
                    peso = float(input())
                    vertex.peso = peso
                    vertex2.peso = peso   
                    #Por nao ser um grafo direcionado, a aresta deve estar nos dois vertices na lista
                    if(grafo.addAresta(vertex, vertex2.copy()) and grafo.addAresta(vertex2, vertex.copy())):
                        print("Aresta adicionada!")
                except ValueError:
                    print("Peso invalido!\n")

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

        elif(key == '7'): #Prim
            print("Deseja substituir o grafo original pela arvore minima? (S/N)")
            resp = str.upper(input())
            if resp == 'S':
                grafo = services.arvore_geradora_minima_prim(grafo)
                grafo.RepresentacaoMatematica()
            elif resp == 'N':
                arv_minima = services.arvore_geradora_minima_prim(grafo)
                arv_minima.RepresentacaoMatematica()
            else:
                print("\nResposta invalida! Escolha novamente.")
            input()
        
        elif(key == '8'):
            print("Insira o vertice de origem:")
            origem = input()
            print("Insira o vertice de destino:")
            destino = input()

            origem = grafo.getVertice(origem)
            destino = grafo.getVertice(destino)

            if(origem == None or destino == None):
                print("Um dos vertices inseridos nao pertencem ao grafo")
            else:
                menor_caminho = dijkstra.Dijsktra(grafo, origem, destino)
                if(menor_caminho.dijsktra_algorithm()):
                    menor_caminho.printa_menor_caminho()
                else:
                    print("Nao existe caminho entre os dois vertices!")
            input()

        elif(key == '9'):
            break
        
        os.system('cls||clear')