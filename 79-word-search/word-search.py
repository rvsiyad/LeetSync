class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rowLength = len(board)
        columnLength = len(board[0])
        path = set()

        def backtrack(r,c,i):
            if i == len(word):
                return True
            
            if r >= rowLength or c >= columnLength or r < 0 or c < 0 or (r,c) in path or word[i] != board[r][c]:
                return False
            
            path.add((r,c))

            result = backtrack(r + 1, c, i + 1) or backtrack(r - 1, c, i + 1) or backtrack(r, c + 1, i + 1) or backtrack(r, c - 1, i + 1)
            path.remove((r,c))

            return result
        
        for R in range(rowLength):
            for C in range(columnLength):
                if backtrack(R,C,0):
                    return True
        
        return False