class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCounter = 0
        perCounter = 0

        for _, num in enumerate(nums):
            if num:
                perCounter += 1
            else:
                maxCounter = max(perCounter, maxCounter)
                perCounter = 0
        
        return max(perCounter, maxCounter)
