class Solution:
    def numDecodings(self, s: str) -> int:
        result = 0
        for i in range(len(s)-1):
            if s[i] != "0":
                result += 1

            num = int(s[i] + s[i+1])



s = Solution()
print(s.numDecodings("abc"))