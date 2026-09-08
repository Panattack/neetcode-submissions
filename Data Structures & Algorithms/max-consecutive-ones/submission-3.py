class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCounter = 0
        preCounter = 0

        for num in nums:
            if num:
                preCounter += 1
            else:
                maxCounter = preCounter if preCounter > maxCounter else maxCounter
                preCounter = 0
        
        return preCounter if preCounter > maxCounter else maxCounter