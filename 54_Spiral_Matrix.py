class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        # # v1
        # i, j = 0, 0
        # width = len(matrix[0])
        # height = len(matrix)
        # result = []
        # starts = (min(width, height) - 1) // 2 + 1
        # if starts == 0: starts = 1
        #
        # for i in range(starts):
        #     j = i
        #     result += matrix[j][i:(width-i)]
        #     for p in range(j+1, height-j):
        #         result.append(matrix[p][width-i-1])
        #
        #     if width*height == len(result):
        #         break
        #
        #     result += matrix[height-j-1][(width-i-2):i:-1]
        #     for p in range(height-j-1, j, -1):
        #         result.append(matrix[p][i])
        #
        # return result

        #v2
        size = len(matrix) * len(matrix[0])
        result = []

        while len(result) < size:
            result += matrix.pop(0)

            for i in matrix:
                result.append(i.pop(-1))

            if len(result) == size: break
            result += matrix.pop(-1)[::-1]

            for i in reversed(matrix):
                result.append(i.pop(0))

        return result

s = Solution()
# print(s.spiralOrder([[1,2,3]]))
# print(s.spiralOrder([[1],[2]]))
# print(s.spiralOrder([[1,2],[3,4],[5,6]]))
# print(s.spiralOrder([[1,2,3,4,5],[6,7,8,9,10]]))
# print(s.spiralOrder([[1,2,3],[4,5,6]]))
# print(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
# print(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9],[10,11,12]]))
# print(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]))
# print(s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
# print(s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))
# print(s.spiralOrder([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]))
# print(s.spiralOrder([[1],[2],[3]]))
print(s.spiralOrder([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]))