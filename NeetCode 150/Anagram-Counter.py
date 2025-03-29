from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # O(1) space assuming hash table will be no higher than 26 characters
        # Assuming lowercase, no symbols
        return Counter(s) == Counter(t)

