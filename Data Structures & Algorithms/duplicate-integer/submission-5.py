class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            curr = nums[i]
            for j in range(len(nums)):
                if i == j: continue
                if curr == nums[j]: return True

        return False