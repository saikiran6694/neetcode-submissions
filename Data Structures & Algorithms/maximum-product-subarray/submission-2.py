class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = nums[0]

        for i in range(len(nums)):
            curr_prod = nums[i]
            max_prod = max(max_prod, curr_prod)
            for j in range(i + 1, len(nums)):
                curr_prod *= nums[j]
                max_prod = max(max_prod, curr_prod)

        return max_prod