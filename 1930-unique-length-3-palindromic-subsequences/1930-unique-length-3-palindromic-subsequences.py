class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans = set()
        n = len(s)

        left = set()
        right = [0] * 26

        
        for ch in s:
            right[ord(ch) - ord('a')] += 1

       
        for i in range(n):
            char = s[i]
          
            right[ord(char) - ord('a')] -= 1

           
            for left_char in left:
                if right[ord(left_char) - ord('a')] > 0:
                    ans.add((left_char, char, left_char))

           
            left.add(char)

        return len(ans)
