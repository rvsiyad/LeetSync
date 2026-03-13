class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smaller_than_pivot = []
        equal_to_pivot = []
        greater_than_pivot = []

        for num in nums:
            if num < pivot:
                smaller_than_pivot.append(num)
            elif num > pivot:
                greater_than_pivot.append(num)
            else:
                equal_to_pivot.append(num)
        
        result = smaller_than_pivot + equal_to_pivot + greater_than_pivot

        return result