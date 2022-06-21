
class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        m = len(mat)
        n = len(mat[0])

        res = []

        for row in range(m):  # process 1st column
            if mat[row][0] == 0:
                res.append(row)
                if len(res) == k: return res

        for col in range(1, n):
            for row in range(m):
                if mat[row][col] == 0 and mat[row][col-1] != 0:
                    res.append(row)
                    if len(res) == k: return res

        for row in range(m):  # process last column
            if mat[row][n-1] == 1:
                res.append(row)
                if len(res) == k: return res

        return res

test_mat = [
    [1,0,0,0],
    [1,1,1,1],
    [1,0,0,0],
    [1,0,0,0]
    ]

solution = Solution()
print(solution.kWeakestRows(test_mat, 2))