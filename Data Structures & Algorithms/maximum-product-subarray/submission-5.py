class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = nums[0]
        curr_min = 1
        curr_max = 1

        for num in nums:
            temp = curr_max * num
            curr_max = max(num * curr_max, num * curr_min, num)
            curr_min = min(temp, num * curr_min, num)

            max_prod = max(curr_max, max_prod)

        return max_prod