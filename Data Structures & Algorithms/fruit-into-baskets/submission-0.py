class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = collections.defaultdict(int)
        l, res, total_count = 0, 0, 0

        for r in range(len(fruits)):
            count[fruits[r]] = 1 + count.get(fruits[r], 0)
            total_count += 1

            while len(count) > 2:
                count[fruits[l]] -= 1
                total_count -= 1

                if count[fruits[l]] == 0:
                    count.pop(fruits[l])

                l += 1

            res = max(total_count, res)
        return res