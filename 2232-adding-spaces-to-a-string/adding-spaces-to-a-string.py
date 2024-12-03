class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        # Turns spaces into a set so can be indexed in O(1) time

        # If i in spaces set, add a space and then the value at i, use a string to keep track
        # Keep appending at index
        newString = ""
        spacesSet = set(spaces)

        i = 0

        while i < len(s):
            if i in spacesSet:
                # Append a space and then the character
                newString += " "
                newString += s[i]
            else:
                newString += s[i]
            i += 1
        
        return newString