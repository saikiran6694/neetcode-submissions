class Solution:
    def mergeAlternately(self, words1: str, words2: str) -> str:
        p1, p2 = 0, 0
        res = ""

        for i in range(len(words1)):
            if p1 < len(words1):
                res += words1[p1]
                p1 += 1
            if p2 < len(words2):
                res += words2[p2]
                p2 += 1

        while p2 < len(words2):
            res += words2[p2]
            p2 += 1

        return res


