class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        n2Pointer = 0

        for i in range(m, len(nums1)):
            nums1[i] = nums2[n2Pointer]
            n2Pointer += 1
        
        nums1.sort()

        