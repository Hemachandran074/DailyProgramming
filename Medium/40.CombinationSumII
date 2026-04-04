#Link: https://leetcode.com/problems/combination-sum-ii/


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def func(candidates, target):
            result = []
            candidates.sort()

            def backtrack(arr, remain, start):
                if remain < 0:
                    return
                
                if remain == 0:
                    result.append(arr[:])
                    return

                for i in range(start, len(candidates)):

                    if i > start and candidates[i] == candidates[i - 1]:
                        continue
                        
                    arr.append(candidates[i])
                    backtrack(arr, remain - candidates[i], i + 1)
                    arr.pop()

            backtrack([], target, 0)
            return result

        return func(candidates, target)
