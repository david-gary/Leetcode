class Solution:
    def generateMatrix(self, n: int):
        # keep track of the start col, end col, start row, and end row
        s_col, s_row, e_col, e_row = 0, 0, n, n
        num = 0

        # make our output matrix to store values in
        out_matrix = []
        for i in range(n):
            out_matrix.append([0]*n)

        while s_col < e_col or s_row < e_row:

            # check the right:
            for col in range(s_col, e_col):
                num += 1
                out_matrix[s_row][col] = num
            s_row += 1

            for row in range(s_row, e_row):
                num += 1
                out_matrix[row][e_col - 1] = num
            e_col -= 1

            for col in range(e_col - 1, s_col - 1, -1):
                num += 1
                out_matrix[e_row - 1][col] = num
            e_row -= 1

            for row in range(e_row - 1, s_row - 1, -1):
                num += 1
                out_matrix[row][s_col] = num
            s_col += 1

        return out_matrix
