class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dfs(r, c, cache):
            if r == (m - 1) and c == (n - 1):
                return 1
            if r >= m or c >= n:
                return 0
            if cache[r][c] != -1:
                return cache[r][c]
            
            cache[r][c] = dfs(r + 1, c, cache) + dfs(r, c + 1, cache)
            return cache[r][c]

        cache = [[-1] * n for _ in range(m)]
        return dfs(0, 0, cache)
        