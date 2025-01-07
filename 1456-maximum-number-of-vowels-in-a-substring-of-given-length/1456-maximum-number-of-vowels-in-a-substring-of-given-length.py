class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a','e','i','o','u'}
        cur_vowels = 0
        mx_vowels = 0

        for i in range(k):
            if s[i] in vowels:
                cur_vowels += 1
        mx_vowels = cur_vowels

        for i in range(k,len(s)):
            if s[i] in vowels:
                cur_vowels += 1
            if s[i-k] in vowels:
                cur_vowels -= 1

            mx_vowels = max(cur_vowels,mx_vowels)

        return mx_vowels