class Solution:
    def isPalindrome(self, s: str) -> bool:
        def create_a_string(s: str):
            res = ""
            for c in s:
                if c.isalnum():
                    res += c
                else:
                    continue

            return res
        
        new_string = create_a_string(s)
        left = 0
        right = len(new_string) - 1
        
        while left <= right:
            if new_string[left].lower() != new_string[right].lower():
                return False
            left += 1
            right -= 1

        return True
