from itertools import product
from typing import List

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def is_happy(s):
            return all(s[i] != s[i + 1] for i in range(len(s) - 1))
        
        happy_strings = sorted(["".join(p) for p in product("abc", repeat=n) if is_happy(p)])
        
        return happy_strings[k - 1] if k <= len(happy_strings) else ""
    
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        num_set = set(nums)
        
        for i in range(2 ** n):
            binary_str = format(i, f'0{n}b')
            if binary_str not in num_set:
                return binary_str
        
        return ""