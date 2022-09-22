class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        width = len(matrix[0])
        height = len(matrix)
        max_len = 1

        for i in range(height):
            for j in range(width):
                if i > 0 and matrix[i-1][j] > matrix[i][j]:
                    print(matrix[i][j])

s = Solution()
s.longestIncreasingPath([[9,9,4],[6,6,8]])