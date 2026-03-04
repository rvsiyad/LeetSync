class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set(['a','e','i', 'o', 'u'])
        prefix_sum = [0] * (len(words) + 1)

        for i in range(len(words)):
            # We need to check if current words has vowels at start and end index
            if words[i][0] in vowels and words[i][-1] in vowels:
                prefix_sum[i + 1] = prefix_sum[i] + 1
            else:
                prefix_sum[i + 1] = prefix_sum[i]
        
        result = []

        for left, right in queries:
            result.append(prefix_sum[right + 1] - prefix_sum[left])
        
        return result