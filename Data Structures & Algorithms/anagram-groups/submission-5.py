class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for string in strs:
            val = "".join(sorted(string))

            if val in d:
                d[val].append(string)
            else:
                d[val] = [string]

        return [s for s in d.values()]