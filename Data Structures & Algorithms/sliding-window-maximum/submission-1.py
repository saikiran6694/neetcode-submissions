class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        l = 0
        for r in range(k, len(nums) + 1):
            max_value = max(nums[l:r])
            res.append(max_value)
            l += 1

        return res





