class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """ 
        temp = [0] * (m + n)

        p1 = 0
        p2 = 0
        temp1 = 0

        while p1 < m and p2 < n:
            if nums1[p1] < nums2[p2]:
                temp[temp1] = nums1[p1]
                p1 += 1
            else:
                temp[temp1] = nums2[p2]
                p2 += 1

            temp1 += 1

        if p1 < m:
            while p1 < m:
                temp[temp1] = nums1[p1]
                temp1 += 1
                p1 += 1

        if p2 < n:
            while p2 < n:
                temp[temp1] = nums2[p2]
                temp1 += 1
                p2 += 1

        for i in range(m + n):
            nums1[i] = temp[i]
            