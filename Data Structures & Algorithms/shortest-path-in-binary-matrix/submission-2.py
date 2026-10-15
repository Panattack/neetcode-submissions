class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        visit = set()
        neighbors = [(-1, 0), (0, -1), (1, 0), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        queue.append((0, 0))
        visit.add((0, 0))
        length = 1

        if grid[ROWS-1][COLS-1] == 1 or grid[0][0]:
            return -1

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()

                if r == ROWS - 1 and c == COLS - 1:
                    return length
                
                for dr, dc in neighbors:
                    if (min(r + dr, c + dc) < 0 or r + dr == ROWS or c + dc == COLS or grid[r + dr][c + dc] == 1 or (r + dr, c + dc) in visit):
                        continue
                    visit.add((r + dr, c + dc))
                    queue.append((r + dr, c + dc))
            length += 1
        
        return -1 
