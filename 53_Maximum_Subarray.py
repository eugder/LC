# Brute-Force, Time Limit Exceeded
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        size = len(nums)
        result = -10000
        for p1 in range(size):
            for p2 in range(p1, size):
                cut = nums[p1:p2+1]
                s = sum(cut)
                if s > result: result = s
                # print(f"p1 - {p1} p2 - {p2} cut - {cut} sum - {s}")
        return result

solution = Solution()
print(solution.maxSubArray([-1]))