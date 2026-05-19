#Link: https://leetcode.com/problems/minimum-common-value/

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)
        n = max(n1, n2)

        i = j = 0

        while i < n > j:
            if i < n1 and j < n2:
                if nums1[i] == nums2[j]:
                    return nums1[i]
                if nums1[i] < nums2[j]:
                    i += 1
                else:
                    j += 1
            else:
                break
        
        return -1
