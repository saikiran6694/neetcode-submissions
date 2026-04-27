class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        firstWord = sorted(s)
        secondWord = sorted(t)

        for i in range(len(s)):
            if firstWord[i] != secondWord[i]:
                return False

        return True