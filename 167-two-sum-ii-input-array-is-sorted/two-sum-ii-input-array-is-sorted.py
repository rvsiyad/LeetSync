class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L = 0
        R = len(numbers) - 1
        currSum = 0

        while L < R:
            currSum = numbers[L] + numbers[R]

            if currSum == target:
                return [L + 1, R + 1]
            elif currSum < target:
                L += 1
            else:
                R -= 1
        
        return []
