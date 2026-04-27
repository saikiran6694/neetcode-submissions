class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        for i in range(len(nums)):
            mult = 1
            for j in range(len(nums)):
                if j == i:
                    continue
                mult *= nums[j]
            res.append(mult)

        return res



