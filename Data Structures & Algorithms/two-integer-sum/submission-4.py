class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i, n in enumerate(nums):
            num = target - n

            if num in d:
                return [d.get(num), i]

            d[n] = i