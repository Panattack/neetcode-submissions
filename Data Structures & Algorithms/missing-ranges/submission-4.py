class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        index = lower
        res = []
        
        if not nums:
            return [[lower, upper]]

        for i in range(0, len(nums)):
            if nums[i] == index:
                index += 1
            else:
                res.append([index, nums[i] - 1])
                index = nums[i] + 1

        if nums[-1] != upper:
            res.append([index, upper])

        return res
