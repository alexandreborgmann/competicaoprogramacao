from typing import List
from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        def children(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
                digit = str((int(lock[i]) - 1 + 10) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
            return res
        q = deque()
        q.append(["0000", 0])
        visit = set(deadends)
        deadens = set()
        while q:
            lock, turns = q.popleft()
            if lock == target:
                return turns
            for child in children(lock):
                if child not in visit:
                    visit.add(child)
                    q.append([child, turns + 1 ])
        return -1

objeto = Solution()
deadends = ["0201","0101","0102","1212","2002"]
target = "0202"
'''
deadends = ["8888"]
target = "0009"
deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]
target = "8888"
'''
print(objeto.openLock(deadends, target))