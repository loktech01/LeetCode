class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums)
        mx = max(freq.values())
        ans = sum(count for num,count in freq.items() if count == mx)
        return ans