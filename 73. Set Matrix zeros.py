class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = []
        column = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0:
                    row.append(i)
                    column.append(j)
        # print(row)
        # print(column)
        for r in row:
            for c in range(len(matrix[r])):
                matrix[r][c] = 0
        for r in range(len(matrix)):
            for c in column:
                matrix[r][c] = 0
        return matrix