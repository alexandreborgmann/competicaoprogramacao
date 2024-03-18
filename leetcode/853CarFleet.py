from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        par = [[p, s] for p,s in zip(position, speed)]

        pilha = []
        for p, s in sorted(par)[::-1]:
            pilha.append((target-p)/s)
            if len(pilha) >=2 and pilha[-1] <= pilha[-2]:
                pilha.pop()
        return(len(pilha))


objeto = Solution()
target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]

'''
target = 10
position = [3]
speed = [3]

target = 100
position = [0,2,4]
speed = [4,2,1]
'''
print(objeto.carFleet(target, position, speed))