class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater_value = [-1] * len(nums2)

        for i in range(len(nums2)):
            curr = nums2[i]

            for j in range(i + 1,len(nums2)):
                if curr < nums2[j]:
                    next_greater_value[i] = nums2[j]
                    break


        res = [-1] * len(nums1)
        for i in range(len(nums1)):
            curr = nums1[i]

            for j in range(len(nums2)):
                if curr == nums2[j]:
                    res[i] = next_greater_value[j]

        return res

