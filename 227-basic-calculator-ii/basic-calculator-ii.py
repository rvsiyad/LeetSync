class Solution:
    def calculate(self, s: str) -> int:
        # We can go over the loop in one pass by keeping track of the curr and prev numbers
        # Use a while loop to loop over to get the numbers and operations
        i = 0

        curr = 0
        prev = 0
        res = 0

        currentOperation = "+"

        while i < len(s):
            currValue = s[i]

            if currValue.isdigit():
                while i < len(s) and s[i].isdigit():
                    curr = curr * 10 + int(s[i])

                    i += 1
                
                i -= 1

                if currentOperation == "+":
                    res += curr
                    prev = curr

                elif currentOperation == "-":
                    res -= curr
                    prev = -curr
                elif currentOperation == "*":
                    res -= prev
                    res += prev * curr

                    prev = curr * prev
                elif currentOperation == "/":
                    res -= prev
                    res += int(prev/curr)

                    prev = int(prev/curr)

                curr = 0
            
            elif currValue != " ":
                currentOperation = currValue
            
            i += 1
        
        return res