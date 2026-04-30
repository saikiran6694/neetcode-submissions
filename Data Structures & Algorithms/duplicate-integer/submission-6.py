class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashMap = {}
        for n in nums:
            hashMap[n] = 1 + hashMap.get(n, 0)

        for key, value in hashMap.items():
            if value > 1:
                return True
        return False
