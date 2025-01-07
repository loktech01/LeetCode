class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        mx = 0
        cur = 0
        for i in gain:
            cur = cur + i
            mx = max(mx,cur)
        return mx