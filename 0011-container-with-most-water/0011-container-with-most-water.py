class Solution:
    def maxArea(self, height: List[int]) -> int:
        mx_area = 0
        n = len(height)
        left,right = 0,n - 1

        while left < right:
            cur_area = min(height[left],height[right]) * (right - left)
            mx_area = max(cur_area,mx_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return mx_area