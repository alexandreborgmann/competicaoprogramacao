import sys

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        sys.set_int_max_str_digits(0)
        stack = []
        for c in num:
            while k > 0 and stack and stack[-1] > c:
                k -= 1
                stack.pop()
            stack.append(c)
            #print(stack,'k=',k,'c=',c,'stack[-1]=',stack[-1])
        stack = stack[:len(stack) - k]
        res = "".join(stack)
        if len(res) == 0:
            return "0"
        return str(int(res))

objeto = Solution()
num = "1432219"
k = 3
num = "10200"
k = 1
num = "10"
k = 2
print(objeto.removeKdigits(num, k))