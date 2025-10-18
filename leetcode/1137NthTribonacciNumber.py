class Solution:
    def tribonacci(self, n: int) -> int:

        if n==0:
            return 0
        if n in (1,2):
            return 1

        s = []
        s.append(0)
        s.append(1)
        s.append(1)


        for i in range(3,n+1):
            v = s[i-3]+s[i-2]+s[i-1]
            s.append(v)
        #print(s,i)
        return(s[-1])


objeto = Solution()
n = 4
n = 25
#n = 20
print(objeto.tribonacci(n))