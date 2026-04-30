class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0

        for i in range(len(nums)):
            curr = nums[i]
            count = 1
            for j in range(len(nums)):
                if i == j: continue
                if curr == nums[j]:
                    count += 1

            if count >= len(nums) / 2: return curr