class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([x.lower() for x in s if 123>ord(x.lower())>96 or 58>ord(x.lower())>47])
        return s == s[::-1]