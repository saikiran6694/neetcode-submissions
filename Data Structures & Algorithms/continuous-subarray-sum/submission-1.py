class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            curr_sum = nums[i]
            for j in range(i + 1, len(nums)):
                curr_sum += nums[j]
                if curr_sum % k == 0:
                    return True

        return False