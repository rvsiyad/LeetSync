class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subSet = []

        def helper(index, total):
            if total == target:
                res.append(subSet.copy())
                return
            
            if index >= len(candidates) or total > target:
                return

            # One subtree, we stay at the index and keep adding
            subSet.append(candidates[index])
            helper(index, total + candidates[index])
            subSet.pop()
            # Another subtree we move the index up one
            helper(index + 1, total)
        
        helper(0, 0)
        return res