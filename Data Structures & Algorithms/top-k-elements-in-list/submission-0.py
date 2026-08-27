class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        if not nums:
            return []
            
        frequency_map = {}
        for num in nums:
            frequency_map[num] = frequency_map.get(num, 0) + 1
            
        sorted_keys = sorted(frequency_map.keys(), key=lambda x: frequency_map[x], reverse=True)
        
        return sorted_keys[:k]