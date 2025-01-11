class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False
        freq_counter = Counter(s)
        odd_freq_counter = sum(1 for count in freq_counter.values() if count % 2 != 0)
        
        return odd_freq_counter <= k