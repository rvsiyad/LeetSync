class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = 0

        # We need to create a hashmap, and add the remainder values to the hashmap
        # Even if the value in the hashamp is remainder 0, still add it, can still create a pair
        
        songRemainders = {}

        for songLength in time:
            if (songLength % 60 == 0):
                count += songRemainders.get(0, 0)
            elif (songLength % 60 != 0):
                count += songRemainders.get((60 - (songLength % 60)), 0)
            
            songRemainders[(songLength % 60)] = 1 + songRemainders.get((songLength % 60), 0)
        
        return count