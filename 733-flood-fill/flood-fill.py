class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(row, column, similarColor, newColor):
            ROWS, COLUMNS = len(image), len(image[0])

            if row < 0 or column < 0 or row == ROWS or column == COLUMNS or image[row][column] != similarColor:
                return
            
            image[row][column] = newColor
            
            dfs(row + 1, column, similarColor, newColor)
            dfs(row - 1, column, similarColor, newColor)
            dfs(row, column + 1, similarColor, newColor)
            dfs(row, column - 1, similarColor, newColor)

        originalColor = image[sr][sc]

        if originalColor != color:
            dfs(sr, sc, originalColor, color)

        return image