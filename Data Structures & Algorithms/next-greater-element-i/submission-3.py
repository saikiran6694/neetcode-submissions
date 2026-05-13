class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1_hashMap = defaultdict(int)
        for i, n in enumerate(nums1):
            num1_hashMap[n] = i

        res = [-1] * len(nums1)
        for i in range(len(nums2)):
            if nums2[i] not in num1_hashMap:
                continue

            for j in range(i + 1, len(nums2)):
                if nums2[i] < nums2[j]:
                    res[num1_hashMap[nums2[i]]] = nums2[j]
                    break

        return res