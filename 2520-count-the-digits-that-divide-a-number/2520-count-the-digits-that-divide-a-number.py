class Solution:
    def countDigits(self, num: int) -> int:
        ans = 0
        for digit in str(num):
            d = int(digit)
            if d != 0 and num % d == 0 :
                ans+= 1
        return ans
        