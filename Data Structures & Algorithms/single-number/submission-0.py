class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor_sum = nums[0]

        for i in range(1, len(nums)):
            xor_sum ^= nums[i]
        
        return xor_sum
