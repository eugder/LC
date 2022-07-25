class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_len = len(s)
        max = 0
        for p1 in range(s_len):
            for p2 in range(p1+1, s_len):
                if s[p2] in s[p1:p2]:
                    if max < p2 - p1:
                        max = p2 - p1
                    break
            else:
                if max < s_len - p1:
                    max = s_len - p1

        return max

s = Solution()
print(s.lengthOfLongestSubstring("abc"))