import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # We use a heap to keep track of the closest to points 0
        # We keep the heap at size k, pop when over k
        # Each point in points, we square the x and y cooirdinates and add toegther, first making them absolute?
        # Add to heap as tuple, first the distance from 0,0 and then the coordinates.
        heap = []

        for x, y in points:
            distanceFromZero = pow(abs(x), 2) + pow(abs(y), 2)

            heapq.heappush(heap, (- distanceFromZero, [x, y]))

            if len(heap) > k:
                heapq.heappop(heap)

        return [coordinates for distance, coordinates in heap]

