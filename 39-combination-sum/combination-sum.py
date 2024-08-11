class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def helper(index, target, curTotal):
            if index >= len(candidates) or curTotal > target:
                return

            if curTotal == target:
                res.append(subset.copy())
                return
            
            subset.append(candidates[index])
            helper(index, target, curTotal + candidates[index])

            subset.pop()
            helper(index + 1, target, curTotal)
        
        helper(0, target, 0)
        return res
            
