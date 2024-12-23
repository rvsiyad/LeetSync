class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = collections.deque()
        L, result = 0, []

        for R in range(len(nums)):
            while queue and nums[queue[-1]] < nums[R]:
                queue.pop()
            
            queue.append(R)

            if L > queue[0]:
                queue.popleft()
            
            if R + 1 >= k:
                result.append(nums[queue[0]])
                L += 1
            
        return result