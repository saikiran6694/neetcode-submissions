class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()

        curr = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if curr == nums[i]:
                count += 1

                if count >= len(nums) / 2: return curr
            else:
                curr = nums[i]
                count = 1

        return curr


