class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        nums_l = len(nums)
        for i in reversed(range(len(nums))):
            if nums[i] == 0:
                nums.pop(i)

        nums.extend([0]*(nums_l - len(nums)))

        return nums

s = Solution()
print(s.moveZeroes([0]))