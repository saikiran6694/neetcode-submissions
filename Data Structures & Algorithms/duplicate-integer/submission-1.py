class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_be = set()

        for n in nums:
            set_be.add(n)

        return True if len(nums) != len(set_be) else False