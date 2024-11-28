class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        if not word:
            return True
        
        def backtrack(r, c, index, path):
            if index >= len(word):
                return True
            
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != word[index] or (r, c) in path:
                return False

            path.add((r, c))
            
            result = backtrack(r + 1, c, index + 1, path) or backtrack(r - 1, c, index + 1, path) or backtrack(r, c + 1, index + 1, path) or backtrack(r, c - 1, index + 1, path)

            path.remove((r, c))
            return result
            
        
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == word[0]:
                    if backtrack(row, col, 0, path):
                        return True
        
        return False