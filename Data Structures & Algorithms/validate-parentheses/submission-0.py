class Solution:
    def isValid(self, s: str) -> bool:
        valid_mappings = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []
        print(stack)

        for c in s:
            if c in list(valid_mappings.values()):
                stack.append(c)
                print(stack)
            
            if c in valid_mappings.keys():
                if not stack:
                    return False
                elif stack[-1] != valid_mappings[c]:
                    return False
                else:
                    stack.pop()
                    print(stack)
        
        print(stack)
        if stack:
            return False
        return True