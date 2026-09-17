class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix, suffix = [0] * len(nums), [0] * len(nums)

        for i in range(1, len(nums)):
            prefix[i] = nums[i - 1] + prefix[i - 1]
            suffix[len(nums) - 1 - i] = nums[len(nums) - i] + suffix[len(nums) - i]
        
        for i in range(len(nums)):
            if suffix[i] == prefix[i]:
                return i

        return -1