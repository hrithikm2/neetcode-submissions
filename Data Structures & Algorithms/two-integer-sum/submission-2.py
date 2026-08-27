class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        i: int = 0
        while i < len(nums):
            offset: Final[Any] = target - nums[i]
            if offset in nums:
                offsetIndex: Final[Any] = nums.index(offset)
                if offsetIndex != i:
                    if i > offsetIndex:
                        return [offsetIndex, i]
                    else:
                        return [i, offsetIndex]
            i += 1
        return []
