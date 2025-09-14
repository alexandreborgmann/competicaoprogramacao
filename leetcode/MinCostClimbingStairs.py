from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)

        #print(cost)
        for i in range(len(cost)-3,-1,-1):
            cost[i] += min( cost[i+1], cost[i+2])
            #print('i=',i,cost[i+1],cost[i+2],cost[i],cost)

        return min(cost[0],cost[1])

objeto = Solution()
cost = [10,15,20]
cost = [1,100,1,1,1,100,1,1,100,1]
print(objeto.minCostClimbingStairs(cost))