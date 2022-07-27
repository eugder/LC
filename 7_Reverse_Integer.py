class Solution:
    def reverse(self, x: int) -> int:
        s = str(abs(x))
        rev = s[::-1]
        res = int(rev)
        if res > 2147483647 or res < -2147483647:
            return 0
        if x < 0:
            res = -res
        return res

s = Solution()
print(s.reverse(-2147483647))