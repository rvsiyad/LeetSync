class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []

        def dfs(i, curr):
            if i == len(s):
                res.append("".join(curr))
                return
            
            if s[i].isalpha():
                curr.append(s[i].upper())
                dfs(i + 1, curr)

                curr.pop()
                curr.append(s[i].lower())
                dfs(i + 1, curr)
            else:
                curr.append(s[i])
                dfs(i + 1, curr)
            
            curr.pop()
        
        dfs(0, [])
        return res