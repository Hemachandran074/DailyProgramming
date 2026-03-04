#Link: https://leetcode.com/problems/special-positions-in-a-binary-matrix/

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row_count = [0] * len(mat)
        col_count = [0] * len(mat[0])
        count = 0

        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 1:
                    row_count[row] += 1
                    col_count[col] += 1

        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 1 and row_count[row] == 1 and col_count[col] == 1:
                    count += 1

        return count
