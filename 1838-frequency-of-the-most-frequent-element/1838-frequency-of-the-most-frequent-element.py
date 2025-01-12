class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left,total,mx_freq = 0,0,0
        for right in range(len(nums)):
            total += nums[right]
            while nums[right] * (right - left + 1) - total > k:
                total -= nums[left]
                left += 1
            mx_freq = max(mx_freq, right - left + 1)
        return mx_freq