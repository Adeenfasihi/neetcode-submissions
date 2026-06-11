import numpy as np

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = []

        for i, num in enumerate(nums):
            array = np.array(nums[0:i]+nums[i+1:])
            product = int(np.prod(array))
            output.append(product)

        return output