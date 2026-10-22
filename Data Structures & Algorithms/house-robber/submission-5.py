class Solution:
    def rob(self, nums: List[int]) -> int:
        # def maxMoney(i, cache):
        #     if i >= len(nums):
        #         return 0
            
        #     if i in cache:
        #         return cache[i]

        #     cache[i] = max(nums[i] + maxMoney(i + 2, cache), maxMoney(i + 1, cache))
        #     return cache[i]

        # cache = {}
        # maxMoney(0, cache)
        # return cache[0]
        
        n = len(nums)
        if not n:
            return 0

        if n <= 2:
            return max(nums)
        
        dp = [0, 0] 
        # 1st position best result up two previous houses,
        # 2nd position best result up to the previous house
        for num in nums:
            tmp = max(dp[0] + num, dp[1])
            dp[0] = dp[1]
            dp[1] = tmp

        return dp[1]
