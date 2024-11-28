class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        combination = []
        
        def backtrack(i, n, k, combination):
            if len(combination) == k:
                result.append(combination.copy())
                return
            
            if i > n:
                return
            
            combination.append(i)
            backtrack(i + 1, n, k, combination)

            combination.pop()
            backtrack(i + 1, n, k, combination)
        
        backtrack(1, n, k, combination)
        return result
