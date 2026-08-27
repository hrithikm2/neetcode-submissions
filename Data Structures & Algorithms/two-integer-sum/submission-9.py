class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #define dictionary 
        mpp = {}

        #run loop to check and insert
        for i in range(0,len(nums)):
            diff = target - nums[i]
            
            if diff in mpp:
                return [mpp[diff], i]
            mpp[nums[i]] = i
        
        return [-1,-1]