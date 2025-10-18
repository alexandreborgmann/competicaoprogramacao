from typing import List
class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        s = list(set(coins))
        resultado = []
        #print(menor, 2 * 7, s)
        for i in range(len(s)):
            for j in range(i, i*k):
                if j <
        return menor

objeto = Solution()
coins = [3,6,9]
k = 3
#coins = [5,2]
#k = 7
print(objeto.findKthSmallest(coins, k))