class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()

        max_con = 0
        for i in range(len(nums)):
            curr = nums[i]
            maxi = 1
            for j in range(i + 1, len(nums)):
                if(nums[j] - curr) == 1:
                    maxi += 1
                    curr = nums[j]
            max_con = max(max_con, maxi)

        return max_con
