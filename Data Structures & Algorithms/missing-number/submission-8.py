class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hypo_sum = 0

        for i in range(len(nums) + 1):
            hypo_sum += i

        actual_sum = 0
        for i in range(len(nums)):
            actual_sum += nums[i]

        return (hypo_sum - actual_sum)
