class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        dict = {}

        def dfs(row, col):
            if (row, col) in dict:
                return dict[(row, col)]
            if col >= len(key):
                return 0
            i = row
            count1 = 0
            count2 = 0
            while True:
                count1 += 1
                if ring[i] == key[col]:
                    break
                i += 1
                i = i % len(ring)
            j = row
            while True:
                count2 += 1
                if ring[j] == key[col]:
                    break
                j -= 1
                if j < 0:
                    j = len(ring) + j
            dict[(row, col)] = min(count1 + dfs(i, col + 1), count2 + dfs(j, col + 1))
            return dict[(row, col)]

        return dfs(0, 0)

objeto = Solution()
ring = "godding"
key = "gd"
#ring = "godding"
#key = "godding"
print(objeto.findRotateSteps(ring, key))