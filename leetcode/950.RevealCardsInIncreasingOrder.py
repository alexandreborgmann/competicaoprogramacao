import collections
from typing import List

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        N = len(deck)
        index = collections.deque(range(N))
        ans = [None] * N
        for card in sorted(deck):
            ans[index.popleft()] = card
            if index:
                index.append(index.popleft())
#            print(index, ans, card)
        return ans


objeto = Solution()
deck = [17,13,11,2,3,5,7]
deck = [1,1000]
print(objeto.deckRevealedIncreasing(deck))