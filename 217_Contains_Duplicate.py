class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        for i in nums:
            if nums.count(i) > 1: return True
        return False

    def containsDuplicate2(self, nums: list[int]) -> bool:
        size = len(nums)
        for i in range(size):
            try:
                ind = nums.index(nums[i], i+1, size)
                return True
            except ValueError:
                pass
        return False

    def containsDuplicate3(self, nums: list[int]) -> bool:
        while len(nums)>1:
            itm = nums.pop(0)
            if itm in nums: return True
        return False

    def containsDuplicate4(self, nums: list[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]: return True
        return False

solution = Solution()
print(solution.containsDuplicate4([1,-1,2,3,-1]))