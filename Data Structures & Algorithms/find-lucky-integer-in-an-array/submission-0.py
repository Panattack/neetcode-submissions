class Solution:
    def findLucky(self, arr: List[int]) -> int:
        countMap = {}

        for a in arr:
            if a not in countMap:
                countMap[a] = 0
            countMap[a] += 1

        res = -1
        for i in countMap:
            if countMap[i] == i:
                res = max(i, res)
        return res
