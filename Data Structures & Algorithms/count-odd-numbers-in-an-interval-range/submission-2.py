class Solution:
    def countOdds(self, low: int, high: int) -> int:
        length = high - low + 1
        res = length // 2

        if high % 2 == 1 and length % 2 == 1:
            res += 1

        return res
        