#Link: https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/

class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        res = []
        n = len(mat[0])
        k = k % n

        for i, row in enumerate(mat):
            if i % 2 == 0:
                r = row[k:] + row[:k]
                res.append(r)
            else:
                l = row[-k:] + row[:-k]
                res.append(l)
        
        return True if res == mat else False
