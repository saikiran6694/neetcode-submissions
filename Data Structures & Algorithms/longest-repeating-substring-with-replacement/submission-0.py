class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0

        for i in range(len(s)):
            hashMap = { s[i] : 1}

            for j in range(i + 1, len(s)):
                hashMap[s[j]] = 1 + hashMap.get(s[j], 0)
            
                other_characters = (j - i + 1) - max(hashMap.values())

                if other_characters <= k:
                    res = max(res, max(hashMap.values()) + other_characters)
        return res