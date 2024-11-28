class Solution:
    def rob(self, nums: List[int]) -> int:
        prevHouse, curHouse = 0, 0

        for num in nums:
            # Either take the sum of the prevHouse and N or we stick with our curHouse
            # We can store this in a temporary variable
            temp = max(prevHouse + num, curHouse)
            # Now we reassign the curSum to the prevHouse value, and the curSum will be the temp
            prevHouse = curHouse
            curHouse = temp
        return curHouse # This will have seen the last value in the array as well.