class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        def check_is_valid_character(c: str):
            return c.isalnum();

        left = 0
        right = len(s) - 1

        while left <= right:
            c_left = s[left]
            c_right = s[right]

            if not check_is_valid_character(c_left):
                left += 1
                continue

            if not check_is_valid_character(c_right):
                right -= 1
                continue

            if c_left.lower() != c_right.lower():
                return False

            left += 1
            right -= 1

        return True
            


