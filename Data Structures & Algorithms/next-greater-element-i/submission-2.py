class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1_hashMap = defaultdict(int)
        for i, n in enumerate(nums1):
            num1_hashMap[n] = i

        res = [-1] * len(nums1)
        for i in range(len(nums2)):
            curr = nums2[i]

            for j in range(i + 1, len(nums2)):
                if curr in num1_hashMap and curr < nums2[j]:
                    res[num1_hashMap[curr]] = nums2[j]
                    break

        return res