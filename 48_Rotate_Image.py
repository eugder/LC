class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        size = len(matrix)

        for i in range(size-1): # diagonal flip
            for j in range(size-i-1):
                matrix[i][j], matrix[size-j-1][size-i-1] = matrix[size-j-1][size-i-1], matrix[i][j]

        for i in range(size//2): # vertical flip
            for j in range(size):
                matrix[i][j], matrix[size-i-1][j] = matrix[size-i-1][j], matrix[i][j]


s = Solution()
s.rotate([[0,1,2,3],[4,5,6,7],[8,9,4,6],[2,3,4,6]])

