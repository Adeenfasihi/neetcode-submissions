class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        result = [1] * n

        prefix = 1
        i = 0
        while i < n:
            result[i] = prefix
            prefix *= nums[i]
            i += 1

        # Suffix pass using while loop
        suffix = 1
        i = n - 1
        while i >= 0:
            result[i] *= suffix
            suffix *= nums[i]
            i -= 1

        return result