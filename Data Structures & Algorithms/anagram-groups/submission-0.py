class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for t in s:
                count[ord(t) - ord("a")] += 1

            hashMap[tuple(count)].append(s)

        return hashMap.values()
        