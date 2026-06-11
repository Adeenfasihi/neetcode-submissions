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
            
            if c in valid_mappings.keys():
                if not stack:
                    return False
                elif stack[-1] != valid_mappings[c]:
                    return False
                else:
                    stack.pop()
        if stack:
            return False
        return True