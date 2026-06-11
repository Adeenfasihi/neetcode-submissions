class Solution:
    def isValid(self, s: str) -> bool:
        valid_mappings = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []

        for c in s:
            if c in list(valid_mappings.values()):
                stack.append(c)
                continue
            
            if not stack:
                return False
            
            if stack[-1] != valid_mappings[c]:
                return False
            
            stack.pop()

        return not stack