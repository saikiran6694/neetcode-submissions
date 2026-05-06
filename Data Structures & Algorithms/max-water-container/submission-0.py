class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum_water_area = 0

        l, r = 0, len(heights) - 1

        while l < r:
            area = min(heights[l], heights[r]) * abs(l - r)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

            maximum_water_area = max(maximum_water_area, area)
        return maximum_water_area