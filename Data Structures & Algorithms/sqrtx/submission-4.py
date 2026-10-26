class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        m = l + (r - l) // 2
        res = 0

        while l <= r:
            if (m * m) == x:
                return m
            if m * m < x:
                res = m
                l = m + 1
            else:
                r = m - 1
            m = l + (r - l) // 2

        return res
