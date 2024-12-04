class Solution:
    def canMatch(self, str1, str2):
        # Check if str1 value matches or can be matched
        if str1 == str2:
            return True
        
        # Can only increment upwards, z becomes a
        if str1 == "z" and str2 == "a":
            return True

        newStr1 = chr(ord(str1) + 1)
        return newStr1 == str2

    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        # We need to check if all elements of str2 can be found in str1
        # For each index in str1, we can increment it up by one.

        # Instead of actually looking for the subtring, we can try and see if the current letter is in
        # str2 or if the incremented letter in the next order is in str2

        # We will use a two pointer approach, one for str1 and another for str2
        # We create a count, increment if cyclic increment is accurate, move both str2 and str1 pointer up
        # If not cyclic or can be achieved by changing, we move pointer up only on str1.

        # Retrun true if count == len(str2)

        count = 0
        s1Pointer, s2Pointer = 0, 0

        while s1Pointer < len(str1) and s2Pointer < len(str2):
            if self.canMatch(str1[s1Pointer], str2[s2Pointer]):
                count += 1
                s1Pointer += 1
                s2Pointer += 1
            else:
                s1Pointer += 1
        
        return count == len(str2)