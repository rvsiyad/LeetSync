class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ROWS = len(board) - 1
        COLUMNS = len(board[0]) - 1

        battleShips = 0

        for row in range(len(board)):
            for column in range(len(board[0])):
                if board[row][column] == "X":
                    if (row + 1) <= ROWS and board[row + 1][column] == "X":
                        nextRow = row + 1
                        while (nextRow) <= ROWS and board[nextRow][column] == "X":
                            board[nextRow][column] = '.'
                            nextRow += 1

                    elif (column + 1) <= COLUMNS and board[row][column + 1] == "X":
                        nextColumn = column + 1
                        while (nextColumn) <= COLUMNS and board[row][nextColumn] == "X":
                            board[row][nextColumn] = '.'
                            nextColumn += 1
                    
                    battleShips += 1
        
        return battleShips
