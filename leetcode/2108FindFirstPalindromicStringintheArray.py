from typing import List

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for w in words:
            if w == w[::-1]:
                return w
        return ""

objeto = Solution()
words = ["abc", "car", "ada", "racecar", "cool"]
#words = ["notapalindrome","racecar"]
#words = ["def","ghi"]
print(objeto.firstPalindrome(words))