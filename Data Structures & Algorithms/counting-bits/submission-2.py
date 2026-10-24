class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 0

        for i in range(1, n + 1):
            print(i, offset, dp)
            if 2 ** (offset + 1) == i:
                offset += 1
            dp[i] = 1 + dp[i - (2 ** offset)]
        
        return dp
    