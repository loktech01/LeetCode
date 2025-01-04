class Solution:
    def reverseVowels(self, s: str) -> str:
       
        vowel = {'a','e','i','o','u','A','E','I','O','U'}
        st = list(s)
        n = len(s)
        temp = []

        for ch in st:
            if ch in vowel:
                temp.append(ch)

        for i in range(n):
            if st[i] in vowel:
                st[i] = temp.pop()

        return ''.join(st)
            
        