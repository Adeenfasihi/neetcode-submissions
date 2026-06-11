# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        
        n   = len(pairs)
        res = [pairs[:]] if pairs else []

        for i in range(1, n):
            current = pairs[i]

            j = i - 1
            while j >= 0 and current.key < pairs[j].key:
                pairs[j], pairs[j+1] = pairs[j+1], pairs[j]
                j -= 1

            # j = i - 1
            # while j > 0 and current.key < pairs[j].key:
            #     j -= 1
            
            # if current.key < pairs[j].key:
            #     pairs.pop(i)
            #     pairs.insert(j, current)

            res.append(pairs[:])
        
        return res