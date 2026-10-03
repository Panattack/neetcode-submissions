class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_rev = 0
        l, r = 0, 1

        while r < len(prices):
            if prices[l] > prices[r]:
                l, r = r, r + 1
                continue
            max_rev = max(max_rev, prices[r] - prices[l])
            r += 1

        return max_rev
