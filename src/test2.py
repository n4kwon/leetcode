# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {'}' : '{', ')' : '(', ']' : '['}
        for c in s:
            if c in mapping: 
                if stack[-1] == mapping[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0



