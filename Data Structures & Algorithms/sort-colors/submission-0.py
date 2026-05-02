class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        bucket = [0] * len([0, 1, 2])
        
        for n in nums:
            bucket[n] += 1
        
        i = 0 
        j = 0
        while j <= 2 and i < len(nums):
            while bucket[j] > 0:
                nums[i] = j
                bucket[j] -= 1
                i += 1

            j += 1

        print(nums) 

