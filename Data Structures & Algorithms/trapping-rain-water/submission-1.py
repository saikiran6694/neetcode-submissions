class Solution:
    def trap(self, height: List[int]) -> int:
        total_water_trapped = 0

        l, r = 0, len(height) - 1

        max_left, max_right = height[l], height[r]

        while l < r:
            if max_left < max_right:
                l += 1
                max_left = max(max_left, height[l])
                total_water_trapped += max_left - height[l]
            else:
                r -= 1
                max_right = max(max_right, height[r])
                total_water_trapped += max_right - height[r]
                
        return total_water_trapped