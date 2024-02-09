import collections
from typing import List

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        paisParaFilhos = collections.defaultdict(list)
        filhosParaPai = {}

        for node in range(n):
            esquerda = leftChild[node]
            direita = rightChild[node]

            if esquerda != -1:
                paisParaFilhos[node].append(esquerda)
                if esquerda not in filhosParaPai:
                    filhosParaPai[esquerda] = node
                else:
                    return False

            if direita != -1:
                paisParaFilhos[node].append(direita)
                if direita not in filhosParaPai:
                    filhosParaPai[direita] = node
                else:
                    return False

            #print('node=', node, 'esquerda=', esquerda, 'direita=', direita, 'paisParaFilhos=', paisParaFilhos,'filhosParaPai=', filhosParaPai)

        raiz = None

        for node in range(n):
            #print('node=', node, 'raiz=', raiz)
            if node not in filhosParaPai:
                if not raiz:
                    raiz = node
                else:
                    return False

        if raiz is None:
            return False

        visitado = set()
        fila = collections.deque([raiz])

        #print('fila=',fila,'visitado=',visitado)

        while fila:
            nodeAtual = fila.popleft()
            visitado.add(nodeAtual)

            for filho in paisParaFilhos[nodeAtual]:
                fila.append(filho)

        return len(visitado) == n

objeto = Solution()
'''
n = 4
leftChild = [1, -1, 3, -1]
rightChild = [2, -1, -1, -1]

n = 4 
leftChild = [1,-1,3,-1] 
rightChild = [2,3,-1,-1]

'''
n = 2 
leftChild = [1,0] 
rightChild = [-1,-1]

print(objeto.validateBinaryTreeNodes(n, leftChild, rightChild))