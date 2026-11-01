class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        t_matrix = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                t_matrix[c][r] = matrix[r][c]
        
        return t_matrix
