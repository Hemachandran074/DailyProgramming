#Link: https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/


class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        
        l1 = list(s1)
        l2 = list(s2)
        
        if l1[0] != l2[0]:
            l2[0], l2[2] = l2[2], l2[0]

        if l1[0] == l2[0]:
            if l1[1] != l2[1]:
                l2[1], l2[3] = l2[3], l2[1]

        if l1 == l2:
            return True
        return False
