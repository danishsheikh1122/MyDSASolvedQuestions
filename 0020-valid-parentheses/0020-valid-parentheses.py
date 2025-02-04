class Solution(object):
    def isValid(self, s):
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in ('(', '[', '{'):
                stack.append(char)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if mapping[char] != top:
                    return False
        return not stack
