class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_set = set()
        column_set = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    row_set.add(i)
                    column_set.add(j)
        for i in row_set:
            matrix[i] = [0]*len(matrix[i])
            
        for i in range(len(matrix)):
            for j in column_set:
                matrix[i][j] = 0
                