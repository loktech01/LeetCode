class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n

        pre = 1
        for i in range(n):
            ans[i] = pre
            pre = pre * nums[i]

        # print(ans)

        suf = 1
        for i in range(n-1,-1,-1):
            ans[i] = ans[i] * suf
            suf = suf * nums[i]
            
        # print(ans)
        return ans