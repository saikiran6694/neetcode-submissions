class Solution:
    def findMin(self, nums: List[int]) -> int:
        mini = nums[0]

        for n in nums[1:]:
            mini = min(mini, n)

        return mini