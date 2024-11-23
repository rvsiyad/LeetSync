class Solution:
    def trap(self, height: List[int]) -> int:
        water_trapped = 0
        L = 0
        R = len(height) - 1

        left_max, right_max = height[L], height[R]

        while L < R:
            if left_max < right_max:
                L += 1
                water_in_area = left_max - height[L]
                if water_in_area > 0:
                    water_trapped += water_in_area
        
                left_max = max(left_max, height[L])
                
            else:
                R -= 1
                water_in_area = right_max - height[R]
                if water_in_area > 0:
                    water_trapped += water_in_area
                right_max = max(right_max, height[R])
                
        
        return water_trapped
