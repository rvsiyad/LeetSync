class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # Two pointer, check values is not between ord('0') and ord('9') if not, check if same, if not same, return False
        # If is a number, do a while loop, 

        wordP, abbrP = 0, 0

        while wordP < len(word) and abbrP < len(abbr):
            if abbr[abbrP].isdigit():
                num = 0

                if abbr[abbrP] == '0':
                    return False

                while abbrP < len(abbr) and abbr[abbrP].isdigit():
                    num = num * 10 + int(abbr[abbrP])

                    abbrP += 1
                
                wordP += num
            else:
                if word[wordP] != abbr[abbrP]:
                    return False
                
                wordP += 1
                abbrP += 1

        if wordP == len(word) and abbrP == len(abbr):
            return True
        
        return False