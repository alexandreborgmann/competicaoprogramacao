from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        resultado = []
        for i in range(len(words)):
            if x in words[i]:
                resultado.append(i)
        return resultado

objeto = Solution()
words = ["leet","code"]
x = "e"
#words = ["abc","bcd","aaaa","cbc"]
#x = "a"
#words = ["abc","bcd","aaaa","cbc"]
#x = "z"
print(objeto.findWordsContaining(words, x))