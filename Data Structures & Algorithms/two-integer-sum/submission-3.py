class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i, n in enumerate(nums):
            num = target - n

            if d.get(num, None) is not None:
                return [d.get(num), i]

            d[n] = i