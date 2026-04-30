class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = -float("inf")

        curr_prod = 1
        for i in range(len(nums)):
            curr_prod = nums[i]
            
            max_prod = max(curr_prod, max_prod)

            for j in range(i + 1, len(nums)):
                curr_prod *= nums[j]
                max_prod = max(curr_prod, max_prod)
        return max_prod
