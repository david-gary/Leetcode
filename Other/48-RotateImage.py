class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left_pos = 0
        right_pos = len(matrix) - 1

        while left_pos < right_pos:
            for i in range(right_pos - left_pos):
                tmp = matrix[left_pos][left_pos + i]
                matrix[left_pos][left_pos + i] = matrix[right_pos - i][left_pos]
                matrix[right_pos - i][left_pos] = matrix[right_pos][right_pos - i]
                matrix[right_pos][right_pos -
                                  i] = matrix[left_pos+i][right_pos]
                matrix[left_pos + i][right_pos] = tmp
            left_pos += 1
            right_pos -= 1
