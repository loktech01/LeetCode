class Solution:
    def compress(self, chars: List[str]) -> int:
        read,write = 0,0
        n = len(chars)
        while read < n:
            char = chars[read]
            count = 0

            while read < n and chars[read] == char:
                read += 1
                count += 1

            chars[write] = char
            write += 1

            if count > 1:
                for d in str(count):
                    chars[write] = d
                    write += 1
        return write