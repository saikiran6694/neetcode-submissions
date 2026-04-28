class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curr_ele = nums[0]
        count = 1

        for i in range(1, len(nums)):
            if nums[i] == curr_ele:
                count += 1
            else:
                count -= 1

            if count <= 0:
                curr_ele = nums[i]
                count = 1

        return curr_ele

        