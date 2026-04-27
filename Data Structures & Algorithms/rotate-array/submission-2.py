class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        l = len(nums)
        no_of_position_shift = l - k
        temp = nums[:no_of_position_shift]
        nums[:k] = nums[no_of_position_shift:]
        nums[k:] = temp
        