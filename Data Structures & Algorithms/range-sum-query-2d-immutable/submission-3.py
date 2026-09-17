class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix_row_sum = []

        for i in range(len(matrix)):
            row_sum = [0] * len(matrix[0])
            total_row = 0
            for j in range(len(matrix[i])):
                total_row += matrix[i][j]
                row_sum[j] = total_row
            self.prefix_row_sum.append(row_sum)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0 
        for i in range(row1, row2 + 1):
            left_prefix = self.prefix_row_sum[i][col1 - 1] if col1 > 0 else 0
            res += self.prefix_row_sum[i][col2] - left_prefix
        return res
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)