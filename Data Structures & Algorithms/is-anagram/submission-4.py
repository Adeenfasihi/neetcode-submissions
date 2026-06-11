class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        d1 = {}

        for char in s:
            d1[char] = d1[char] + 1 if d1.get(char) else 1
        
        for char in t:
            d1[char] = d1[char] - 1 if d1.get(char) else -1

        for key, val in d1.items():
            if val != 0:
                return False

        return True
        