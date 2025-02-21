from itertools import product
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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

class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.values = set()
        
        def recover(node, value):
            if not node:
                return
            node.val = value
            self.values.add(value)
            recover(node.left, 2 * value + 1)
            recover(node.right, 2 * value + 2)
        
        recover(root, 0)
    
    def find(self, target: int) -> bool:
        return target in self.values
