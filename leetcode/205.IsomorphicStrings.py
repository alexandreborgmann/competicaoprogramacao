class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        lookup = {}
        rlookup = {}
        for sc, tc in zip(s,t):
            if sc not in lookup:
                lookup[sc] = tc
            if tc not in rlookup:
                rlookup[tc] = sc
            print(sc,tc,lookup,rlookup)
            if lookup[sc]!= tc or rlookup[tc] != sc:
                return False
        return True

objeto = Solution()
#s = "egg"
#t = "add"
s = "foo"
t = "bar"
#s = "paper"
#t = "title"
print(objeto.isIsomorphic(s, t))