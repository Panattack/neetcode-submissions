class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        right_max = [0] * n
        right_max[-1] = nums[-1]
        suffix_sum = nums[-1]

        for i in range(n - 2, -1, -1):
            suffix_sum += nums[i]
            right_max[i] = max(right_max[i + 1], suffix_sum)
        
        cur_sum = 0
        prefix_sum = 0
        max_sum = nums[0]

        for i in range(n):
            prefix_sum += nums[i]
            cur_sum = max(cur_sum, 0) + nums[i]
            max_sum = max(cur_sum, max_sum)
            if i + 1 < n:
                max_sum = max(max_sum, prefix_sum + right_max[i + 1])
        
        return max_sum
