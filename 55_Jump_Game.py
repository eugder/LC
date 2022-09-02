class Solution:
    # v1 with recursion (Time Limit)
    # def canJump(self, nums: list[int]) -> bool:
    #     if len(nums) == 1: return True
    #     def one_jump(idx):
    #         for i in range(idx):
    #             if nums[i] >= idx-i:
    #                 if i == 0:
    #                     raise Exception
    #                 one_jump(i)
    #
    #     try:
    #         one_jump(len(nums)-1)
    #     except:
    #         return True
    #     return False

    # v2
    def canJump(self, nums: list[int]) -> bool:
        if len(nums) == 1: return True
        scope = 0
        for i in range(len(nums)):
            if i > scope:
                return False
            dist = nums[i] + i
            if scope < dist:
                scope = dist
                if scope >= len(nums)-1:
                    return True


s = Solution()
# print(s.canJump([2,3,1,1,4]))
# print(s.canJump([3,2,1,0,4]))
print(s.canJump([5,2,0,4,0,1,0,1]))
# print(s.canJump([0]))
# print(s.canJump2())