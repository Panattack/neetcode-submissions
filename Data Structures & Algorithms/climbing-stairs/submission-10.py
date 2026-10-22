class Solution:
    # def climbStairs(self, n: int) -> int:
    #     if n < 0:
    #         return 0
    #     elif n == 0:
    #         return 1
    #     return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    def climbStairs(self, n: int) -> int:
        def memoization(n, cache):
            if n < 0:
                return 0
            if n == 0 or n == 1:
                return 1
            if n in cache:
                return cache[n]
            cache[n] = memoization(n-1, cache) + memoization(n - 2, cache)
            return cache[n]

        cache = {}
        res = memoization(n, cache)
        return res
