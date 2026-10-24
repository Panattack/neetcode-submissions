class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid) - 1, len(obstacleGrid[0]) - 1
    
        if obstacleGrid[rows][cols] == 1 or obstacleGrid[0][0] == 1:
            return 0

        obstacleGrid[rows][cols] = 1

        for r in range(rows, -1, -1):
            for c in range(cols, -1, -1):
                if r == rows and c == cols:
                    continue

                if obstacleGrid[r][c] == 1:
                    obstacleGrid[r][c] = 0
                else:
                    down = obstacleGrid[r + 1][c] if r + 1 <= rows else 0
                    right = obstacleGrid[r][c + 1] if c + 1 <= cols else 0
                    obstacleGrid[r][c] = down + right

        return obstacleGrid[0][0]
