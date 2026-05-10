class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        tCount, window = {}, {}

        for c in t:
            tCount[c] = 1 + tCount.get(c, 0)

        have, need = 0, len(tCount)
        res, resLen = [-1, -1], float("inf")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in tCount and window[c] == tCount[c]:
                have += 1

            while have == need:
                # update our result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)

                # pop from the left of our window
                window[s[l]] -= 1

                if s[l] in tCount and window[s[l]] < tCount[s[l]]:
                    have -= 1
                l += 1

        return s[res[0]: res[1] + 1]



        

        