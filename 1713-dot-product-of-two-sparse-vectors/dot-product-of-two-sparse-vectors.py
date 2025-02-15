class SparseVector:
    def __init__(self, nums):
        self.validNums = collections.defaultdict(int)

        for i, num in enumerate(nums):
            if num:
                self.validNums[i] = num
        
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        product = 0

        for key, value in self.validNums.items():
            if key in vec.validNums:
                product += value * vec.validNums[key]
        
        return product
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)