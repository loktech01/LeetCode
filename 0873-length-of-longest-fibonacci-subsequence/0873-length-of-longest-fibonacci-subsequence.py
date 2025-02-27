from typing import List

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        index_map = {val: i for i, val in enumerate(arr)}  # Map value to index
        n = len(arr)
        dp = {}
        max_length = 0

        # Iterate through all pairs (j, i) with j < i
        for i in range(n):
            for j in range(i):
                x = arr[i] - arr[j]  # The potential previous Fibonacci number
                if x < arr[j] and x in index_map:  # Ensure it's a valid Fibonacci-like sequence
                    k = index_map[x]
                    dp[j, i] = dp.get((k, j), 2) + 1  # Extend the sequence
                    max_length = max(max_length, dp[j, i])

        return max_length if max_length >= 3 else 0
