class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        hashMapS = {}
        hashMapT = {}

        for n in s:
            if n in hashMapS:
                hashMapS[n] += 1
            else:
                hashMapS[n] = 1

        for n in t:
            if n in hashMapT:
                hashMapT[n] += 1
            else:
                hashMapT[n] = 1

        

        for keys in hashMapS:
            if keys not in hashMapT:
                return False

            if hashMapT[keys] != hashMapS[keys]:
                return False

        return True
