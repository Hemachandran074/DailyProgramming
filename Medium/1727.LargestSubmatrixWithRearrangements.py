#Link: https://leetcode.com/problems/largest-submatrix-with-rearrangements/

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        max_area = 0
        heights = [0] * n

        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 1:
                    heights[col] += 1
                else:
                    heights[col] = 0

            heights_sort = sorted(heights, reverse = True)
            
            for i in range(len(heights_sort)):
                max_area = max(max_area, heights_sort[i] * (i + 1))

        return max_area
