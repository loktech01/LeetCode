from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        odd_count = 0  # Count of prefix sums that are odd
        even_count = 1  # Starts with 1 since prefix sum = 0 (which is even)
        prefix_sum = 0
        result = 0

        for num in arr:
            prefix_sum += num  # Update prefix sum
            
            if prefix_sum % 2 == 0:  # Even prefix sum
                result = (result + odd_count) % MOD
                even_count += 1
            else:  # Odd prefix sum
                result = (result + even_count) % MOD
                odd_count += 1

        return result
