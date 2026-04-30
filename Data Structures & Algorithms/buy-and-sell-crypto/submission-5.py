class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        max_prof = 0
        left, right = 0, 1

        while left <= right and right < len(nums):
            curr_prof = nums[right] - nums[left]

            if nums[left] > nums[right]:
                left = right
            elif curr_prof > max_prof:
                max_prof = curr_prof
                
            right += 1
        return max_prof