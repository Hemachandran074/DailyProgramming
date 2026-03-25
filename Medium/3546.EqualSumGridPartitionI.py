#Link: https://leetcode.com/problems/equal-sum-grid-partition-i/

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total_sum = 0
        r = len(grid)
        c = len(grid[0])

        row_sum = []
        col_sum = []

        for i in range(r):
            for j in range(c):
                total_sum += grid[i][j]

        if total_sum % 2 != 0:
            return False

        for i in range(r):
            r_sum = 0
            for j in range(c):
                r_sum += grid[i][j]
            row_sum.append(r_sum)

        for j in range(c):
            c_sum = 0
            for i in range(r):
                c_sum += grid[i][j]
            col_sum.append(c_sum)
        
        mid = total_sum // 2
        
        s = 0
        for num in row_sum:
            s += num
            if s == mid:
                return True

        s = 0
        for num in col_sum:
            s += num
            if s == mid:
                return True
        
        return False
