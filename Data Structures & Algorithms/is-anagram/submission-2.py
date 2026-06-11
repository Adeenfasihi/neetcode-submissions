class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        d1 = {}
        d2 = {}

        for char in s:
            d1[char] = d1[char] + 1 if d1.get(char) else 1
        
        for char in t:
            d2[char] = d2[char] + 1 if d2.get(char) else 1

        return d1==d2
        