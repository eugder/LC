class Solution:
    def  divide(self, dividend: int, divisor: int) -> int:

        res = 0
        minus = False

        if divisor < 0:
            divisor = -divisor
            minus = not minus
        if dividend < 0:
            dividend = -dividend
            minus = not minus
        buf = divisor

        if dividend >= 2147483648 and not minus:
            return 2147483647
        if dividend >= 2147483648 and minus:
            return -2147483648

        while buf <= dividend:
            buf += divisor
            res += 1

        if minus:
            res = -res

        return res

s = Solution()
print(s.divide(-2147483649,1))