class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashMap:
                return [min(i, hashMap[diff]), max(i, hashMap[diff])]
            hashMap[nums[i]] = i

    