class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        telephone = {
            '2' : ["a","b","c"],
            '3' : ["d","e","f"],
            '4' : ["g","h","i"],
            '5' : ["j","k","l"],
            '6' : ["m","n","o"],
            '7' : ["p","q","r", "s"],
            '8' : ["t","u","v"],
            '9' : ["w","x","y", "z"],
        }

        res = []

        def helper(i, combination):
            if i >= len(digits):
                res.append(combination)
                return
            
            for c in telephone[digits[i]]:
                helper(i + 1, combination + c)
        
        helper(0, "")
        return [] if res == [""] else res
