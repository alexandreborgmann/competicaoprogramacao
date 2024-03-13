from typing import List
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        res = score = 0
        tokens.sort()

        l, r = 0, len(tokens) - 1
        while l < r:
            if power >= tokens[l]:
                power -= tokens[l]
                l += 1
                score += 1
                res = max(res, score)
            elif score > 0:
                power += tokens[r]
                r -= 1
            else:
                break
        return res


objeto = Solution()
tokens = [100]
power = 50
#tokens = [200,100]
#power = 150
#tokens = [100,200,300,400]
#power = 200
print(objeto.bagOfTokensScore(tokens, power))