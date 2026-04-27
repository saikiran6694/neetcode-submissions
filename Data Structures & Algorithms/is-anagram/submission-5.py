class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap = {}

        for c in s:
            hashMap[c] = 1 + hashMap.get(c, 0)

        for c in t:
            if c in hashMap:
                hashMap[c] -= 1
            else:
                hashMap[c] = 1

        for key, value in hashMap.items():
            if value > 0:
                return False

        return True