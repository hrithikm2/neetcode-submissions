class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        visitedNumbers = dict()
        i: int = 0
        for i in range(len(nums)):
            number: Final[int] = nums[i]
            complement: Final[int] = target - number
            if complement in visitedNumbers:
                return [visitedNumbers[complement], i]
            else:
                visitedNumbers[number] = i
            i += 1
        return []