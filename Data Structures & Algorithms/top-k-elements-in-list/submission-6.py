class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            hashMap[n] = 1 + hashMap.get(n, 0)

        for n, c in hashMap.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, -1, -1):
            for j in range(len(freq[i])):
                res.append(freq[i][j])
                if len(res) == k:
                    return res

        