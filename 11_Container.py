class Solution:
    def maxArea(self, height: list[int]) -> int:
        i = 0
        j = len(height) - 1
        m = 0
        while i < j:
            mi = min(height[i], height[j])
            m = max(m, (j - i) * mi)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return m

s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))
