class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        freshCount = self.findFreshAndRottenFruits(grid, queue)
        ROWS, COLS = len(grid), len(grid[0])
        neighbors = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        visit = set()
        length = 0

        # if no fresh fruit from the start, return 0
        if not freshCount:
            return 0

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in neighbors:
                    if (min(r + dr, c + dc) < 0 or r + dr == ROWS or c + dc == COLS or (r + dr, c + dc) in visit 
                        or grid[r + dr][c + dc] == 2 or grid[r + dr][c + dc] == 0):
                        continue
                    freshCount -= 1
                    queue.append((r + dr, c + dc))
                    visit.add((r + dr, c + dc))
            length += 1
        
        return length - 1 if not freshCount else -1

    def findFreshAndRottenFruits(self, grid, queue) -> int:
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))
        return fresh
