class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Determines if two strings are anagrams of each other.
        An anagram uses the exact same characters with the same frequencies.
        """
        # If lengths differ, they cannot be anagrams.
        if len(s) != len(t):
            return False

        char_frequency = {}
        for char_s, char_t in zip(s, t):
            # Increment char_frequency for s
            char_frequency[char_s] = char_frequency.get(char_s, 0) + 1

            # Decrement char_frequency for t
            char_frequency[char_t] = char_frequency.get(char_t, 0) - 1

        # Check if all the keys have value 0 in char_frequency
        return all(count == 0 for count in char_frequency.values())