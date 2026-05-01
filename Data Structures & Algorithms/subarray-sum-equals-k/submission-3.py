class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curr = 0
        prefix_sum = { 0: 1}

        for n in nums:
            curr += n
            diff = curr - k

            res += prefix_sum.get(diff, 0)
            prefix_sum[curr] = 1 + prefix_sum.get(curr, 0)
        return res

