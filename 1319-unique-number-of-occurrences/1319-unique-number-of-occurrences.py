from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = Counter(arr)                    # Count frequency of each number
        occurrences = list(freq.values())      # Extract frequencies
        return len(occurrences) == len(set(occurrences))  # Check if all frequencies are unique
