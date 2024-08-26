class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []

        for i in nums:
            minHeap.append(i * -1)
        
        heapq.heapify(minHeap)
        res = 0

        while k > 0:
            res = heapq.heappop(minHeap) * -1
            k -= 1
        
        return res