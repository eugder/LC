
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_note_lst = list(magazine) # with list is faster
        for i in ransomNote:
            try:
                pos = ransom_note_lst.index(i)
                del(ransom_note_lst[pos])
            except ValueError:
                return False
        return True


construct_checker = Solution()
print(construct_checker.canConstruct("aabc", "abbc"))