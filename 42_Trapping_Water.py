class Solution:
    def trap(self, height: list[int]) -> int:
        m = max(height)
        peak = height.index(m)
        volume = 0
        i = 0

        while i<peak:
            lvl = height[i]
            i += 1
            while height[i] < lvl:
                volume += lvl - height[i]
                i += 1

        back = height[peak:]
        back.reverse()
        #print(back)

        i = 0

        while i<len(back)-1:
            lvl = back[i]
            i += 1
            while back[i] < lvl:
                volume += lvl - back[i]
                i += 1

        return volume

s = Solution()
print(s.trap([4,2,0,3,2,5]))