class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        # Basic Approach =======================
        # Got TLE
        # for i in range(len(nums) - 2):
        #     for j in range(i+1,len(nums)-1):
        #         for k in range(j+1, len(nums)):
        #             if nums[i] < nums[j] and nums[j] < nums[k]:
        #                 return True
        # return False
        # ==========================================

        # Easy way
        first = float('inf')
        second = float('inf')

        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False