class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        max_right_sum = sum(nums)
        max_left_sum = 0

        for i in range(len(nums)):
            if i == 0:
                max_right_sum -= nums[i]
                if max_right_sum == max_left_sum:
                    return i
            else:
                max_left_sum += nums[i - 1]
                max_right_sum = (max_right_sum - nums[i])
                if max_right_sum == max_left_sum:
                    return i
        return -1

        # for i in range(len(nums)):
        #     if i == 0:
        #         max_right_sum -= nums[i]
        #         if max_right_sum == max_left_sum:
        #             return i
        #     else:
        #         max_right_sum = (max_right_sum - max_left_sum - nums[i])
        #         max_left_sum += nums[i - 1]
        #         if max_right_sum == max_left_sum:
        #             return i
        #         # else:
        #         #     max_right_sum = (max_right_sum - max_left_sum - nums[i])
        #         #     max_left_sum += nums[i - 1]

        # return -1
        

