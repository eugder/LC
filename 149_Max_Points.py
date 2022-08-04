class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        max_points = 1
        for i in range(len(points)-1):
            for j in range(i+1, len(points)):
                max_points = max(max_points, self.points_number(points, i, j))
        return max_points

    def points_number(self, points, i, j):
        points_on_line = 0
        for p in points:
            if self.if_belongs(p, points[i], points[j]):
                points_on_line += 1
        return points_on_line

    def if_belongs(self, p, i, j):
        x1 = j[0] - i[0]
        x2 = p[0] - i[0]
        y1 = j[1] - i[1]
        y2 = p[1] - i[1]
        return ((x1*y2 - x2*y1) == 0)

s = Solution()
print(s.maxPoints([[1,1]]))
