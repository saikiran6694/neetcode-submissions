class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)

        for i in range(len(nums1)):
            curr_num1 = nums1[i]

            for j in range(len(nums2)):
                if curr_num1 == nums2[j]:
                    for k in range(j + 1, len(nums2)):
                        if curr_num1 < nums2[k]:
                            res[i] = nums2[k]
                            break

        return res
