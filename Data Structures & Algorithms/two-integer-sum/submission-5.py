class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}

        for i, num in enumerate(nums):
            diff = target - num
            res = num_dict.get(diff)

            if res is not None:
                return [res, i]
            else:
                num_dict[num] = i
            
        return []