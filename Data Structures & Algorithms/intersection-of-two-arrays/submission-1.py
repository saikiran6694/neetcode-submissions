class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = set()
        res = set()

        for n in nums1:
            s.add(n)

        for n in nums2:
            if n in s:
                res.add(n)
        return list(res)
