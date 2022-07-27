class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums = nums1 + nums2
        sorted_nums = sorted(nums)
        sorted_len = len(sorted_nums)
        if sorted_len%2 > 0:
            return float(sorted_nums[sorted_len//2])
        else:
            n1 = sorted_nums[sorted_len//2 - 1]
            n2 = sorted_nums[sorted_len//2]
            return float((n1 + n2)/2)

s = Solution()
print(s.findMedianSortedArrays([0], [0]))