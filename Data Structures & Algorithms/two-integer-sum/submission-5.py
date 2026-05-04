class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashMap:
                mini = min(i, hashMap.get(diff, 0))
                maxi = max(i, hashMap.get(diff, 0))
                return [mini, maxi]
            hashMap[n] = i
    