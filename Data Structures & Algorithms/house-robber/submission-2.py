class Solution:
    def rob(self, nums: List[int]) -> int:
        def maxMoney(i, cache):
            if i >= len(nums):
                return 0
            
            if i in cache:
                return cache[i]

            cache[i] = max(nums[i] + maxMoney(i + 2, cache), maxMoney(i + 1, cache))
            return cache[i]

        cache = {}
        maxMoney(0, cache)
        return cache[0]