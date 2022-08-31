class Solution:
    def myPow(self, x: float, n: int) -> float:
        y = bin(abs(n))
        result = 1
        f = x
        for i in reversed(y[2:]):
            if i == "1":
                result *= f
            f *= f

        if n < 0:
            result = 1/result

        return result

s = Solution()
print(s.myPow(2,-2))