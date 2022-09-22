class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        # v1 MemoryError
        sky_map = []
        for i in buildings:
            if i[1] > (len(sky_map) - 1):
                sky_map.extend([0]*(i[1] - len(sky_map) + 1))
            for j in range(i[0], i[1]+1):
                if sky_map[j] < i[2]:
                    sky_map[j] = i[2]

        sky_map.append(0)
        result = []
        for i in range(-1,len(sky_map)-1):
            if sky_map[i+1] > sky_map[i]:
                result.append([i+1,sky_map[i+1]])
            if sky_map[i+1] < sky_map[i]:
                result.append([i,sky_map[i+1]])

        return result

s = Solution()
# print(s.getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))
# print(s.getSkyline([[0,2,3],[2,5,3]]))
print(s.getSkyline([[0,2,3]]))