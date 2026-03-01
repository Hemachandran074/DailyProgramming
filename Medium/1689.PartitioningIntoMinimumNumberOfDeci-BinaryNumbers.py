#Link: https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/

class Solution:
    def minPartitions(self, n: str) -> int:
        mini = float('-inf')
        for i in n:
            num = int(i)

            if num > mini:
                mini = num

        return mini
