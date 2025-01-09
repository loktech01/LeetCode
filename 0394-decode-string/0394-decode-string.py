class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_string = ''
        current_digit = 0

        for ch in s:
            if ch.isdigit():
                current_digit = current_digit * 10 + int(ch)
            elif ch == '[':
                stack.append((current_string,current_digit))
                current_digit = 0
                current_string = ''
            elif ch == ']':
                prev_string , num = stack.pop()
                current_string = prev_string + current_string * num
            else:
                current_string += ch

        return current_string