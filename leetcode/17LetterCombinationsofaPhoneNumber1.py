from typing import List
import itertools
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        m = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        return ["".join(a) for a in itertools.product(*[m[d] for d in digits])]

objeto = Solution()
digits ="234"
#digits = "23"
#digits = ""
#digits = "2"
print(objeto.letterCombinations(digits))