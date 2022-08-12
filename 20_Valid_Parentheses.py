class Solution:
    def  isValid(self, s: str) -> bool:
        lst = [x for x in s]
        l = len(s)
        stop_mark = False

        if l%2 > 0: return False

        while not stop_mark:
            stop_mark = True
            for i in range(1, len(lst)):
                if (lst[i] == ')' and lst[i-1] == '(') or (lst[i] == '}' and lst[i - 1] == '{') or (lst[i] == ']' and lst[i - 1] == '['):
                    lst.pop(i)
                    lst.pop(i-1)
                    stop_mark = False
                    break


        return len(lst) == 0


s = Solution()
print(s.isValid("{[]}"))