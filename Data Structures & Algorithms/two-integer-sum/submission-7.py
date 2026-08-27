class Solution:
    def twoSum(self, input_nums: list[int], input_target: int) -> list[int]:
        seen = {}
        for i, num in enumerate(input_nums):
            complement = input_target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []
