class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curr = nums[0]
        count = 1

        for n in nums:
            if curr == n:
                count += 1
            elif count == 0:
                count = 1
                curr = n
            else:
                count -= 1

        return curr


