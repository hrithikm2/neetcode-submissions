class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        visitedNumbers: Final[Any] = {}
        i: int = 0
        while i < len(nums):
            number: Final[Any] = nums[i]
            complement: Final[Any] = target - number
            if complement in visitedNumbers and visitedNumbers[complement] != None:
                return [visitedNumbers[complement], i]
            else:
                visitedNumbers[number] = i
            i += 1
        return []