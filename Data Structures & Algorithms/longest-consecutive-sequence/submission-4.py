class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n_set = set(nums)
        res = 0

        for n in nums:
            # check if its start of a sequence
            if (n - 1) not in n_set:
                length = 1
                while (n + length) in n_set:
                    length += 1

                res = max(length, res)
        return res
            