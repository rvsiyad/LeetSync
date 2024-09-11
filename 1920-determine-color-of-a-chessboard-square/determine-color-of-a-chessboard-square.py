class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        letterToNum = {
            "a": 1,
            "b": 2,
            "c": 3,
            "d": 4,
            "e": 5,
            "f": 6,
            "g": 7,
            "h": 8,
        }

        x = letterToNum[coordinates[0]]
        y = int(coordinates[1])

        if x % 2 == 0 and y % 2 == 0:
            return False
        
        if x % 2 != 0 and y % 2 == 0:
            return True

        if x % 2 == 0 and y % 2 != 0:
            return True
        
        if x % 2 != 0 and y % 2 != 0:
            return False