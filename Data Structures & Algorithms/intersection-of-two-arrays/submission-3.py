class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1_set = set()
        n2_set = set()

        for n1 in nums1: n1_set.add(n1)
        for n2 in nums2: n2_set.add(n2)

        res = []
        for n1 in n1_set:
            if n1 in n2_set:
                res.append(n1)
        return res