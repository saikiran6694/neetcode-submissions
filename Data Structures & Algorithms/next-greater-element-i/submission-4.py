class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1_hashMap = defaultdict(int)
        for i, n in enumerate(nums1):
            num1_hashMap[n] = i

        res = [-1] * len(nums1)
        stack = []

        for i in range(len(nums2)):
            curr = nums2[i]

            while stack and curr > stack[-1]:
                val = stack.pop()
                idx = num1_hashMap[val]
                res[idx] = curr

            if curr in num1_hashMap:
                stack.append(curr)

        return res