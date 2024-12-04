class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        groupedAnagrams = {}

        for s in strs:
            # We can either create a hashmap or sort them, lets first sort
            original = tuple(sorted(s))

            if original in groupedAnagrams:
                groupedAnagrams[original].append(s)
            else:
                groupedAnagrams[original] = [s]
        
        print(groupedAnagrams)

        for key, value in groupedAnagrams.items():
            result.append(value)
        
        return result