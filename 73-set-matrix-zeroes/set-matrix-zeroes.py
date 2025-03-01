class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # Multiple postion DFS
        # Find all positions where there is a 0. Add to a list
        # Iterate over the list, and make all values in its rows and cols 0
        # Create 4 seperate functions to ammend the row/col in all 4 directions
        ROWS, COLS = len(matrix), len(matrix[0])

        positionOfZeros = []

        for row in range(ROWS):
            for col in range(COLS):
                if matrix[row][col] == 0:
                    positionOfZeros.append([row, col])
        
        for row, col in positionOfZeros:
            self.zerosUp(row, col, matrix)
            self.zerosDown(row, col, matrix)
            self.zerosLeft(row, col, matrix)
            self.zerosRight(row, col, matrix)
        
    def zerosUp(self, row, col, matrix):
        ROWS, COLS = len(matrix), len(matrix[0])
        
        if row < 0 or row >= ROWS or col < 0 or col >= COLS:
            return

        matrix[row][col] = 0

        self.zerosUp(row - 1, col, matrix)
    
    def zerosDown(self, row, col, matrix):
        ROWS, COLS = len(matrix), len(matrix[0])
        
        if row < 0 or row >= ROWS or col < 0 or col >= COLS:
            return

        matrix[row][col] = 0

        self.zerosDown(row + 1, col, matrix) 
    
    def zerosLeft(self, row, col, matrix):
        ROWS, COLS = len(matrix), len(matrix[0])
        
        if row < 0 or row >= ROWS or col < 0 or col >= COLS:
            return

        matrix[row][col] = 0

        self.zerosLeft(row, col - 1, matrix) 
    
    def zerosRight(self, row, col, matrix):
        ROWS, COLS = len(matrix), len(matrix[0])
        
        if row < 0 or row >= ROWS or col < 0 or col >= COLS:
            return

        matrix[row][col] = 0

        self.zerosRight(row, col + 1, matrix) 