class Solution:
    def trap(self, height: List[int]) -> int:
        # water_trapped = 0
        # L = 0
        # R = len(height) - 1

        # left_max, right_max = height[L], height[R]

        # while L < R:
        #     if left_max < right_max:
        #         L += 1
        #         water_in_area = left_max - height[L]
        #         if water_in_area > 0:
        #             water_trapped += water_in_area
        
        #         left_max = max(left_max, height[L])
                
        #     else:
        #         R -= 1
        #         water_in_area = right_max - height[R]
        #         if water_in_area > 0:
        #             water_trapped += water_in_area
        #         right_max = max(right_max, height[R])
                
        
        # return water_trapped

        prefix = [0] * len(height)

        maxHeightLeft = 0
        # Prefix
        for i in range(len(height)):
            prefix[i] = maxHeightLeft
            maxHeightLeft = max(maxHeightLeft, height[i])

        # Postfix
        maxHeightRight = 0
        postfix = [0] * len(height)

        for i in range(len(height) -1, -1, -1):
            postfix[i] = maxHeightRight
            maxHeightRight = max(maxHeightRight, height[i])

        maxAreaOfWater = 0
        # pick min val for both and take maxAreaOfWater
        for i in range(len(height)):
            minHeight = min(prefix[i], postfix[i])
            water_can_hold = minHeight - height[i]

            if water_can_hold > 0:
                maxAreaOfWater += water_can_hold
        
        return maxAreaOfWater
