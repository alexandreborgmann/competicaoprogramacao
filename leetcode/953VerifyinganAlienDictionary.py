from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        self.order_dict ={ letter: i for i, letter in enumerate(order)}
        #print(self.order_dict)
        for word1, word2 in zip(words, words[1:]):
            if not self.words_are_lexico(word1, word2):
                return False
        return True

    def words_are_lexico(self, word1, word2):
        for i in range(min(len(word1),len(word2))):
            if self.order_dict[word1[i]] != self.order_dict[word2[i]]:
                if self.order_dict[word1[i]] < self.order_dict[word2[i]]:
                    return True
                else:
                    return False
        return len(word1) <= len(word2)

objeto = Solution()
words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
#words = ["word", "world", "row"]
#order = "worldabcefghijkmnpqstuvxyz"
#words = ["apple","app"]
#order = "abcdefghijklmnopqrstuvwxyz"
print(objeto.isAlienSorted(words, order))