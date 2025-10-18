from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append([t, i])
        return(res)

objeto = Solution()
#temperatures = [73,74,75,71,69,72,76,73]
#temperatures = [30,40,50,60]
temperatures = [30,60,90]
print(objeto.dailyTemperatures(temperatures))
