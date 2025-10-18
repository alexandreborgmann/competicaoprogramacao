from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maior = 0
        for i in range(len(accounts)):
            soma = sum(accounts[i])
            if maior < soma:
                maior = soma
        return maior

objeto = Solution()
#accounts = [[1,2,3],[3,2,1]]
#accounts = [[1,5],[7,3],[3,5]]
accounts = [[2,8,7],[7,1,3],[1,9,5]]
print(objeto.maximumWealth(accounts))
