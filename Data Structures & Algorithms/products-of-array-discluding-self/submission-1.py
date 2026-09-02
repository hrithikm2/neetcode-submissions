class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [1] * n
        
        prefix = 1
        for i in range(n):
            if i == 0:
                result[i] = 1
            else:
                prefix *= nums[i - 1]
                result[i] = prefix
                
        postfix = 1
        for i in range(n - 1, -1, -1):
            if i == n - 1:
                result[i] *= 1
            else:
                postfix *= nums[i + 1]
                result[i] *= postfix
                
        return result