class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        m = len(accounts)
        n = len(accounts[0])

        res = 0

        for row in range(m):
            one_res = 0
            for val in accounts[row]:
                one_res = one_res + val
            if one_res > res: res = one_res

        return res

test_mat = [
    [2,8,7],
    [7,1,3],
    [1,9,5]
    ]

solution = Solution()
print(solution.maximumWealth(test_mat))