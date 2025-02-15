class Solution(object):
    def wordBreak(self, s, wordDict):
        queue = collections.deque()
        visited = set()

        queue.append(s)

        while queue:
            subString = queue.popleft()

            if subString in visited:
                continue
            
            if subString == "":
                return True
        
            visited.add(subString)
            
            for word in wordDict:
                if subString.startswith(word):
                    queue.append(subString[len(word):])

        return False