from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while stones and len(stones)>1:
            stones.sort()
            #print(stones,stones[-1], stones[-2])
            if stones[-2] == stones[-1]:
                stones.pop(-1)
                stones.pop(-1)
            else:
                stones[-1] = stones[-1] - stones[-2]
                stones.pop(-2)
            #print('depois',stones)
        if len(stones) == 0:
            return 0
        else:
            return stones[0]

objeto = Solution()
stones = [2,7,4,1,8,1]
#stones = [1]
#stones = [2,2]
print(objeto.lastStoneWeight(stones))