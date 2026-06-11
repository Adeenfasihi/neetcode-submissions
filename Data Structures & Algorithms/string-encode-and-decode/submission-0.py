class Solution:
    delimiter = "#"

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for string in strs:
            hashed_string = string
            length = len(hashed_string)
            encoded_string = encoded_string + str(length) + self.delimiter + hashed_string
        
        return encoded_string


    def decode(self, s: str) -> List[str]:
        word_list = []
        sub_string = ""

        i = j = 0
        length = ""

        while i < len(s):
            while s[i] != self.delimiter:
                length += s[i]
                i += 1
            
            i += 1
            j = i
            
            while j < i + int(length):
                sub_string += s[j]
                j += 1
            
            i += int(length)
            
            word_list.append(sub_string)

            length = ""
            sub_string = ""
            
        
        return word_list
