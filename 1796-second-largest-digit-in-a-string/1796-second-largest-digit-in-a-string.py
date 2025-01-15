import heapq
class Solution:
    def secondHighest(self, s: str) -> int:
        digits = set([int(ch) for ch in s if ch in "0123456789"]) 
        if len(digits) > 0:
            digits.remove(max(digits))
            if len(digits) > 0:
                return max(digits)
            else:
                return -1
        return -1