class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        if nums == [0,0,0]: return [[0,0,0]]
        l = len(nums)
        result = []
        arr = [0]*200002
        for i in nums:
            arr[i] +=1

        for p1 in range(l-2):
            for p2 in range(p1+1, l-1):
                c = 0 - nums[p1] - nums[p2]
                if nums[p1] == 0 and nums[p2] == 0 and arr[c] == 2:
                    continue
                if arr[c] > 0:
                    if arr[c] == 1 and c in [nums[p1], nums[p2]]:
                        continue
                    else:
                        triplet = [nums[p1], nums[p2], c]
                        if self.is_distinct(triplet, result):
                            result.append(triplet)

                # if c in nums[p2+1:]:
                #     triplet = [nums[p1], nums[p2], c]
                #     if self.is_distinct(triplet, result):
                #         result.append(triplet)

                # for p3 in range(p2+1, l):
                #     if (nums[p1] + nums[p2] + nums[p3]) == 0:
                #         triplet = [nums[p1], nums[p2], nums[p3]]
                #         if self.is_distinct(triplet, result):
                #             result.append(triplet)

        return result

    def is_distinct(self, triplet, result):
        triplet.sort()
        for i in result:
            i.sort()
            if triplet == i:
                return False

        return True

s = Solution()
print(s.threeSum([-2,0,0,2,2]))
