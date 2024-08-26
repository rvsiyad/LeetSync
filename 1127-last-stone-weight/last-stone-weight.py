class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Make all values in the stones negative, works as a maxHeap in python
        # Heapify the new list
        # While the loop has more than 1 value
            # Then we pop the values and mulitplyy by -1
            # If x > y: append x - y and multiply the sum by -1
            # Elif y > x: append y - x and multiply the sum by -1
            # If equal, carry on
        # If heap not empty: return heap.pop(), else return 0

        minHeap = []
        
        for i in stones:
            minHeap.append(i * -1)
        
        heapq.heapify(minHeap)

        while len(minHeap) > 1:
            x = heapq.heappop(minHeap) * -1
            y = heapq.heappop(minHeap) * -1

            if x > y:
                value = (x - y) * -1
                heapq.heappush(minHeap, value)
            elif y > x:
                value = (y - x) * -1
                heapq.heappush(value)
        
        if minHeap:
            return heapq.heappop(minHeap) * -1
        else:
            return 0


