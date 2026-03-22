#Link: https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

class Solution:

    def rotation(self, mat):

        n = len(mat)

        for i in range(n):
            for j in range(i, n):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
            
        for row in range(n):
            mat[row].reverse()

    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4):
            if mat == target:
                return True
            self.rotation(mat)
        
        return False
