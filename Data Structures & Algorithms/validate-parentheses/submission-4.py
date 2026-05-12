class Solution:
    def isValid(self, s: str) -> bool:
        paranthesis = { "}": "{", "]": "[", ")": "("}
        stack = []

        for c in s:
            if c in paranthesis:
                if stack and stack[-1] == paranthesis[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False

