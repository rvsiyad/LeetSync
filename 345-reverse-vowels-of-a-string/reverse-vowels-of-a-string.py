class Solution:
    def reverseVowels(self, s: str) -> str:
        sAsList = list(s)
        L = 0
        R = len(sAsList) - 1

        vowels = set('aeiouAEIOU')

        print("Before while", sAsList)

        while L < R:
            while L < R and sAsList[L] not in vowels:
                L += 1
            
            while L < R and sAsList[R] not in vowels:
                R -= 1
            
            sAsList[L], sAsList[R] = sAsList[R], sAsList[L]
        
            L += 1
            R -= 1
        
        print("After while", sAsList)

        return ''.join(sAsList)

        
