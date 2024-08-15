class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if bills[0] != 5:
            return False
    
        fiveDollars = 0
        tenDollars = 0

        for bill in bills:
            if bill == 5:
                fiveDollars += 1
            elif bill == 10:
                if fiveDollars > 0:
                    fiveDollars -= 1
                else:
                    return False
                tenDollars += 1
            else:
                if fiveDollars > 0 and tenDollars > 0:
                    fiveDollars -= 1
                    tenDollars -= 1
                elif fiveDollars > 2:
                    fiveDollars -= 3
                else:
                    return False
        
        return True