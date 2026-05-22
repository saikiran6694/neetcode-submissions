class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c == "]":
                char = ""
                while stack and stack[-1] != "[":
                    pop_char = stack.pop()
                    if pop_char.isalpha():
                        char = pop_char + char

                if stack[-1] == "[":
                    stack.pop()
                    number = ""

                    while stack and stack[-1].isdigit():
                        number = stack.pop() + number

                    number = number

                    number = int(number)
                    char = number * char
                    stack.append(char)

            else:
                stack.append(c)

            print(stack)

        return "".join(stack)