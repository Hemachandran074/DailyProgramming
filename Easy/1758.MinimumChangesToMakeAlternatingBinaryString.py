#Link: https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/

class Solution:
    def minOperations(self, s: str) -> int:
        str0 = ""
        str1 = ""
        count0 = 0
        count1 = 0

        for i in range(len(s)):
            if i % 2 == 0:
                str1 += "1"
                str0 += "0"
            else:
                str0 += "1"
                str1 += "0"
            if str1[i] != s[i]:
                count1 += 1
            if str0[i] != s[i]:
                count0 += 1
        
        return min(count0, count1)
