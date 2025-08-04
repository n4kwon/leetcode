class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {']' : '[', '}': '{', ')' : '('}

        for c in s:
            if c in mapping: # check if character is closing parentheses
                if stack and stack[-1] == mapping[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0
