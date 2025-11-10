class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s1 = list(s.split(" "))
        sRetorno = " ".join(s1[:k])
        return(sRetorno)

objeto = Solution()
'''
s = "Hello how are you Contestant"
k = 4
s = "What is the solution to this problem"
k = 4
'''
s = "chopper is not a tanuki"
k = 5
print(objeto.truncateSentence(s, k))