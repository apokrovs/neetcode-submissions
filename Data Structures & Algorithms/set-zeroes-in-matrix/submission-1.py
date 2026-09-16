from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix or not matrix[0]:
            return
        
        R = len(matrix)
        C = len(matrix[0])
        first_col_zero = False

        # 1. Flag zero positions in first row and first column
        for i in range(R):
            if matrix[i][0] == 0:
                first_col_zero = True
            for j in range(1, C):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # 2. Update submatrix based on indicators
        for i in range(1, R):
            for j in range(1, C):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # 3. Update first row if matrix[0][0] was flagged
        if matrix[0][0] == 0:
            for j in range(C):
                matrix[0][j] = 0

        # 4. Update first column if first_col_zero was flagged
        if first_col_zero:
            for i in range(R):
                matrix[i][0] = 0