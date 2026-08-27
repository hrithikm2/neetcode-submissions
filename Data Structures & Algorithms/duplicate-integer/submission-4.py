class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        # number as key mapped to count as value
        valuesSet = set()
        for number in nums:
            if number in valuesSet:
                return True
            else:
                valuesSet.add(number)
        return False