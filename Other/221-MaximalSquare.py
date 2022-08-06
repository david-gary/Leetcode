class Solution:
    def maximalSquare(self, matrix) -> int:
        MAT_ROWS = len(matrix)
        MAT_COLS = len(matrix[0])

        areas = {}

        def scan(row, col):
            if row >= MAT_ROWS or col >= MAT_COLS:
                return 0

            if (row, col) not in areas:
                down = scan(row + 1, col)
                right = scan(row, col + 1)
                diagonal = scan(row+1, col+1)

                areas[(row, col)] = 0

                if matrix[row][col] == "1":
                    areas[(row, col)] = 1 + min(down, right, diagonal)

            return areas[(row, col)]

        scan(0, 0)
        return max(areas.values()) ** 2
