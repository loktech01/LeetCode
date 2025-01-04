class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x,y=0,0
        n = len(nums)
        while x < n:
            if nums[x] == 0:
                while y < n:
                    if nums[y] != 0:
                        nums[x],nums[y] = nums[y],nums[x]
                        break
                    y += 1
            x += 1
            y += 1
        

        