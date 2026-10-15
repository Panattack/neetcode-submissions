class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        count = 0

        def dfs(i, j):
            ROWS, COLS = len(grid), len(grid[0])
            if min(i, j) < 0 or i == ROWS or j == COLS or (i, j) in visit or grid[i][j] == "0":
                return
            visit.add((i, j))
            
            dfs(i - 1, j)
            dfs(i, j - 1)
            dfs(i + 1, j)
            dfs(i, j + 1)
            

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visit and grid[i][j] == "1":
                    count += 1
                    dfs(i, j)

        return count
