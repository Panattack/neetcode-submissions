class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visit = set()

        def dfs(r, c) -> int:
            ROWS, COLS = len(grid), len(grid[0])
            if min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visit or grid[r][c] == 0:
                return 0
                
            visit.add((r, c))
            count = 1
            count += dfs(r - 1, c)
            count += dfs(r, c - 1)
            count += dfs(r + 1, c)
            count += dfs(r, c + 1)

            return count
        
        maxCount = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) not in visit and grid[r][c] == 1:
                    maxCount = max(maxCount, dfs(r, c))

        return maxCount