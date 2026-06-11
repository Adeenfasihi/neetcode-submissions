class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}

        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        
        d = sorted(d.items(), key=lambda item: item[1], reverse=True)

        return [d[i][0] for i in range(k)]

        
        
