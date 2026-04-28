class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            curr_majority = nums[i]
            count = 1
            for j in range(len(nums)):
                if i == j: continue
                if nums[j] == curr_majority:
                    count += 1

            if count >= len(nums) / 2:
                return curr_majority
        return -1