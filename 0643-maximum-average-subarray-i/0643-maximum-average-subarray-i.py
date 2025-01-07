class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur_window = sum(nums[:k])
        mx = cur_window

        for i in range(k,len(nums)):
            cur_window = cur_window + nums[i] - nums[i-k]
            mx = max(mx,cur_window)

        return mx/k
        