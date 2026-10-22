class Solution:
    # def climbStairs(self, n: int) -> int:
    #     if n < 0:
    #         return 0
    #     elif n == 0:
    #         return 1
    #     return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    # def climbStairs(self, n: int) -> int:
    #     def memoization(n, cache):
    #         if n < 0:
    #             return 0
    #         if n == 0 or n == 1:
    #             return 1
    #         if n in cache:
    #             return cache[n]
    #         cache[n] = memoization(n-1, cache) + memoization(n - 2, cache)
    #         return cache[n]

    #     cache = {}
    #     res = memoization(n, cache)
    #     return res

    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        dp = [1, 2]

        i = 3
        while i <= n:
            tmp = dp[1]
            dp[1] = dp[0] + dp[1]
            dp[0] = tmp
            i += 1

        return dp[1]
