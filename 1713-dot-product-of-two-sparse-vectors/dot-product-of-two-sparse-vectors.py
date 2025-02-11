"""
We know that anything times zero, will return 0.
When we intialise the sparseVector, create a hashmap corrisponding to index at which to multiply by.
Is maybe a list of lists better?
"""
class SparseVector:
    def __init__(self, nums: List[int]):
        self.arr = []

        for i in range(len(nums)):
            if nums[i]:
                self.arr.append((i, nums[i]))
    
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        total = 0

        i, j = 0, 0

        while i < len(self.arr) and j < len(vec.arr):
            iIndex, iValue = self.arr[i]
            jIndex, jValue = vec.arr[j]

            if iIndex == jIndex:
                total += (iValue * jValue)
                i += 1
                j += 1
            elif iIndex < jIndex:
                i += 1
            else:
                j += 1

        return total

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)