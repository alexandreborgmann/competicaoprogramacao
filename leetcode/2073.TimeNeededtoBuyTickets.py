from typing import List
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        soma = 0
        while tickets[k] != 0:
            for i in range(len(tickets)):
                if tickets[i] != 0:
                    tickets[i] -= 1
                    soma += 1
                    if tickets[k] == 0:
                        break
                i += 1
        return soma

objeto = Solution()
tickets = [2,3,2]
k = 2
#tickets = [5,1,1,1]
#k = 0
print(objeto.timeRequiredToBuy(tickets, k))