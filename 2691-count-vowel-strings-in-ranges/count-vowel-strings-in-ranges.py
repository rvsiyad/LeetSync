class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # Solution 2:
        # Get the prefix sum and compute from that
        """
        Prefix sum = [0, 1, 1, 2, 3]
        """
        vowels = set(['a','e','i','o','u'])

        prefix = [0] * (len(words) + 1)

        for i in range(len(words)):
            prefix[i + 1] = prefix[i]

            word = words[i]
            if word[0] in vowels and word[-1] in vowels:
                prefix[i + 1] += 1
        
        result = []

        for start, end in queries:
            validWords = prefix[end + 1] - prefix[start]
            result.append(validWords)
        
    
        return result
        # Solution 1:
        # Queries is across all the words, 0 indexed.
        # Return the number of words that start and end with a vowel
        # We should go through each word, see if starts and end with a vowel.
        # Need to find a time efficenet way to return if the number of words within that range
        # Since we dont care about the acutal words, we just need to know if true or false, return count of trues within a range?
        
        # vowels = set(['a','e','i','o','u'])
        # containsVowelIndex = []

        # for i in range(len(words)):
        #     word = words[i]
        #     if word[0] in vowels and word[-1] in vowels:
        #         containsVowelIndex.append(True)
        #     else:
        #         containsVowelIndex.append(False)
        
        # result = []

        # for start, end in queries:
        #     count = 0

        #     for i in range(start, end + 1):
        #         if containsVowelIndex[i] == True:
        #             count += 1
            
        #     result.append(count)
        
        # return result

