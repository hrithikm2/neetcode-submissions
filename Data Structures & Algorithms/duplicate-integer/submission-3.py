class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        # number as key mapped to count as value
        valueMapping = {}
        for number in nums:
            if number in valueMapping:
                valueMapping[number] += 1
                if valueMapping[number] > 1:
                    return True
            else:
                valueMapping[number] = 1
        return False