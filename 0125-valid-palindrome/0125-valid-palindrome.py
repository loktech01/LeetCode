class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_string = ''.join(ch.lower() for ch in s if ch.isalnum())
        return clean_string == clean_string[::-1]
