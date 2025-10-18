from collections import Counter, defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        buckets = defaultdict(list)
        #print(count, buckets)

        for char, cnt in count.items():
            buckets[cnt].append(char)

        res = ""
        for i in range(len(s),0,-1):
            for c in buckets[i]:
                res += c * i
        return res

s = "tree"
#s = "cccaaa"
#s = "Aabb"

objeto = Solution()
print(objeto.frequencySort(s))