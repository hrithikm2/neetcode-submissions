class Solution:

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        group_anagrams_map = defaultdict(list)

        for word in strs:
            char_frequency = [0] * 26

            for char in word:
                index = ord(char) - ord("a")
                char_frequency[index] += 1


            key = tuple(char_frequency)
            group_anagrams_map[key].append(word)
        result = list(group_anagrams_map.values())
        return result
