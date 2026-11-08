class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        res = 0

        for i in range(rows):
            res += mat[i][i]
            res += mat[i][rows - 1 - i]
        if rows & 1:
            res -= mat[rows // 2][rows // 2]
        return res
