class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        global_min, global_max = nums[0], nums[0]
        cur_min, cur_max = 0, 0
        total = 0

        for num in nums:
            total += num
            cur_min = min(cur_min + num, num)
            cur_max = max(cur_max + num, num)
            global_min = min(global_min, cur_min)
            global_max = max(global_max, cur_max)

        return max(global_max, total - global_min) if global_max > 0 else global_max
