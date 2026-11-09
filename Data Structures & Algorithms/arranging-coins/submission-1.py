class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 1, n
        func = lambda x: x * (x + 1) // 2

        while l <= r:
            m = l + (r - l) // 2
            res = func(m)
            if res == n:
                return m
            elif res > n:
                r = m - 1
            else:
                l = m + 1
        
        return r