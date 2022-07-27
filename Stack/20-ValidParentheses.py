class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matchBracket = {")": "(", "]": "[", "}": "{"}

        for char in s:
            if char in matchBracket:
                if stack and stack[-1] == matchBracket[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return bool(len(stack))
