class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        
        if numRows == 1:
            return [[1]]
        
        rows = 1

        res = [[1]]
    
        while rows < numRows:
            lastRow = res[-1]

            newRow = []

            L = 0
            R = 1

            newRow.append(1)
            while R < len(lastRow):
                newRow.append(lastRow[L] + lastRow[R])
                R += 1
                L += 1
            
            newRow.append(1)

            res.append(newRow)
            rows += 1

        return res