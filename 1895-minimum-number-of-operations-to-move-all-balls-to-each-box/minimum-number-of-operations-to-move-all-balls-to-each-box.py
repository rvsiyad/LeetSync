class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # Return array to move all boxes to ith index in boxes array
        # 1 Equals  that ith index contains a ball, 0 means it does not

        # Initial approach, get the index of all 1s, for each index, find the absolute difference between itself and remaining ones.
        # That would be a O(n^2) time operation though.

        indexOfOnes = []

        for i in range(len(boxes)):
            if boxes[i] == "1":
                indexOfOnes.append(i)
        
        # Get absolute difference between all values and the index
        print(indexOfOnes)
        result = []

        for i in range(len(boxes)):
            moves = 0

            for index in indexOfOnes:
                moves += abs(i - index)
            
            result.append(moves)
        
        return result

        # Prefix sum second approach
        """
        boxes = "110"

        prefix = [0, 1, 2]
        suffix = [1, 0, 0]
        """