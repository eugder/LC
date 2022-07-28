class Solution:
    def myAtoi(self, s: str) -> int:
        ready_s = s.strip()
        start = 0
        result  = ""
        if len(ready_s) == 0:
            return 0
        if ready_s[0] == "-":
            start = 1
            result = "-"
        if ready_s[0] == "+":
            start = 1
        for i in range(start, len(ready_s)):
            if ready_s[i].isdecimal():
                result += ready_s[i]
                i += 1
            else:
                break
        if result == "" or result == "-":
            result = "0"

        int_result = int(result)
        if int_result > 2147483647:
            int_result = 2147483647
        if int_result < -2147483648:
            int_result = -2147483648
        return int_result

s = Solution()
print(s.myAtoi(" "))
