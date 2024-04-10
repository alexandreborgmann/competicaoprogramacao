from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)

        def get_prefix_max(h):
            prefix = [0]
            for i in range(N):
                prefix.append(max(h[i], prefix[-1]))
            return prefix

        left = get_prefix_max(height)
        #print(left)
        right = get_prefix_max(height[::-1])[::-1]
        #print(right)
        water = 0
        for i in range(N):
            water += max(min(left[i], right[i + 1]) - height[i],0)
            #print('left[i]=',left[i],'right[i + 1]=',right[i + 1],'height[i]=',height[i],'water=',water)
        return water

objeto = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
height = [4,2,0,3,2,5]
print(objeto.trap(height))
