class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_map = {}
        nums2_map = {}

        for n1 in nums1:
            nums1_map[n1] = 1 + nums1_map.get(n1, 0)
        
        for n2 in nums2:
            nums2_map[n2] = 1 + nums2_map.get(n2, 0)
        
        res = []
        for key in nums1_map:
            if key in nums2_map:
                res.append(key)

        return res