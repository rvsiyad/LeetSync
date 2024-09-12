class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Set = set(nums1)

        res = set()

        for i in nums2:
            if i not in res and i in nums1Set:
                res.add(i)
        
        return list(res)