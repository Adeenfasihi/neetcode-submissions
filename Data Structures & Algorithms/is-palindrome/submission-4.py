class Solution:
    def isPalindrome(self, s: str) -> bool:
        splitted = "".join([x for x in s.lower() if 123>ord(x)>96 or 58>ord(x)>47])
        return splitted == splitted[::-1]