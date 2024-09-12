class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1Arr = s1.split(" ")
        s2Arr = s2.split(" ")

        res = []

        s1Count, s2Count = {}, {}

        for i in s1Arr:
            s1Count[i] = 1 + s1Count.get(i, 0)
        
        for i in s2Arr:
            s2Count[i] = 1 + s2Count.get(i, 0)
        
        for word in s1Arr:
            if s1Count[word] == 1 and word not in s2Count:
                res.append(word)

        # Check for uncommon words in s2Arr
        for word in s2Arr:
            if s2Count[word] == 1 and word not in s1Count:
                res.append(word)

        return res