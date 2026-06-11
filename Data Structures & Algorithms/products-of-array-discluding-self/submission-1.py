class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = []

        for i, num in enumerate(nums):
            array = nums[0:i]+nums[i+1:]
            product = 1
            for i in array:
                product *= i
            output.append(product)

        return output