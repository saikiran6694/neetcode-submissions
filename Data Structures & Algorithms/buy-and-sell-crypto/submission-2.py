class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        max_prof = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                curr_prof = nums[j] - nums[i]

                max_prof = max(max_prof, curr_prof)

        return max_prof