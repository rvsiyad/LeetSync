class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        if (word and not abbr) or (abbr and not word):
            return False

        wP, aP = 0, 0

        while wP < len(word) and aP < len(abbr):
            if abbr[aP].isdigit():
                num = 0

                if abbr[aP] == '0':
                    return False
                
                while aP < len(abbr) and abbr[aP].isdigit():
                    num = num * 10 + int(abbr[aP])

                    aP += 1
                
                wP += num

            else:
                if word[wP] != abbr[aP]:
                    return False
            
                aP += 1
                wP += 1
        
        return wP == len(word) and aP == len(abbr)

                

