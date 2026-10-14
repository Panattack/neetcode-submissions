class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])
        if color == image[sr][sc]:
            return image
            
        def dfs(image, r, c, color, val):
            if min(r, c) < 0 or r == ROWS or c == COLS or val != image[r][c]:
                return

            image[r][c] = color

            dfs(image, r - 1, c, color, val)
            dfs(image, r, c - 1, color, val)
            dfs(image, r + 1, c, color, val)
            dfs(image, r, c + 1, color, val)

        dfs(image, sr, sc, color, image[sr][sc])

        return image