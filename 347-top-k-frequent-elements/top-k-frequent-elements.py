import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}

        heap = []

        for num in nums:
            counter[num] = 1 + counter.get(num, 0)
        
        for value, count in counter.items():
            heapq.heappush(heap, (count, value))

            if len(heap) > k:
                heapq.heappop(heap)
        
        result = [ value for count, value in heap]
        return result
        