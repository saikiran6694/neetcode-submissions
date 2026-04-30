class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = nums[0]
        curr_min = 1
        curr_max = 1

        for i in range(len(nums)):
            temp = curr_max * nums[i]
            curr_max = max(nums[i], curr_max * nums[i], curr_min * nums[i])
            curr_min = min(nums[i], temp, curr_min * nums[i])

            max_prod = max(curr_max, max_prod)
        return max_prod
