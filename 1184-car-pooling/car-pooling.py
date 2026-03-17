'''
- Given capacity for a car. No of seats it can hold
- We are also given a a trips array
- Trips[i] contains = [numPassengers, fromI, toI]
- They only travel east, to the right.
- Return True if possible to pikc up and drop off all people
- We will work of the assumption that the from and to are constantyly increasing.

Example:
trips = [[2,1,5],[3,3,7]], capacity = 4

car = 5

Figuring out a solution:
- We can check at what index we can remove the previous pasengers, we can keep track of that via hashmap
- Check if start and previous values are overlapping, similar to intervals
- We can create a prefix, if check if end location of prev and start of next overlap, if so we need to 
increase the prefix sum, else we start from the current intervals overlap.
'''
import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips = sorted(trips, key=lambda x: x[1])
        # We need to remove customers once they have reached there destination
        # We can do this via a minHeap, where the values into the minHeap are the end time and the num of passengers dropped off.
        # We can then pop and use a while loop to remove values.

        prefix_sum = [0] * (len(trips) + 1)
        heap = []

        for i in range(len(trips)):
            # Look at the current trip and the next trip
            num_passengers, start, end = trips[i]

            # If maxEnd is greater than the current start, there is an overlap
            prefix_sum[i + 1] = prefix_sum[i] + num_passengers
            
            while heap and heap[0][0] <= start:
                prefix_sum[i + 1] -= heap[0][1]
                heapq.heappop(heap)

            if prefix_sum[i + 1] > capacity:
                return False

            heapq.heappush(heap, (end, num_passengers))
        return True