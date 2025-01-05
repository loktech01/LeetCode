class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        delta = [0] * (n+1)

        for start,end,direction in shifts:
            if direction  == 1:
                delta[start] += 1
                delta[end + 1] -= 1
            else:
                delta[start] -= 1
                delta[end +1] += 1
        print(delta)

        cum_shift = 0
        for i in range(n):
            cum_shift += delta[i]
            delta[i] = cum_shift

        result = []
        for i,ch in enumerate(s):
            shift = delta[i] % 26
            new_char = chr((ord(ch) - ord('a')+ shift) % 26 + ord('a'))
            result.append(new_char)
        return ''.join(result)
