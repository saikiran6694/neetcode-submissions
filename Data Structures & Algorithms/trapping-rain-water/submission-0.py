class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)

        max_left = 0
        max_right = 0

        min_of_Left_and_right = [0] * len(height)

        # calculate the maxlefts
        for i in range(1, len(height)):
            curr_left = height[i - 1]

            if curr_left > max_left:
                max_left = curr_left
                maxLeft[i] = curr_left
            else:
                maxLeft[i] = max_left

        for i in range(len(height) - 2, -1, -1):
            curr_right = height[i + 1]

            if curr_right > max_right:
                max_right = curr_right
                maxRight[i] = curr_right
            else:
                maxRight[i] = max_right

        for i in range(len(height)):
            min_of_Left_and_right[i] = min(maxLeft[i], maxRight[i])


        total_water_trapped = 0


        for i, h in enumerate(height):
            trapped_water = min_of_Left_and_right[i] - h
            if trapped_water >= 0:
                total_water_trapped += trapped_water

        return total_water_trapped
        

        

