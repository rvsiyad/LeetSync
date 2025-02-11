class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # All characters are unique in order
        """
        Since all characters are unique, iterate over the order string, adding to a hashmap the index it belongs to
        this will give us the heirarchy of characters in the string. Save as character : order.

        String s, count occurences of each character, append it x times to string?
        """
        # Count occurences of each character:
        charCount = {}

        for char in s:
            charCount[char] = 1 + charCount.get(char, 0)
        
        newString = ""

        for char in order:
            if char in charCount:
                count = charCount.get(char, 0)

                newString += char * count
                del charCount[char]
        
        for char, count in charCount.items():
            newString += char * count
        
        return newString

        

