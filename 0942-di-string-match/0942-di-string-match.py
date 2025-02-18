class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        # stack = []
        # result = []
        # num = 0
        # for i in range(len(s)+1):
        #     stack.append(num)
        #     num += 1

        #     if i == len(s) or s[i] == 'I':
        #         while stack:
        #             result.append(stack.pop())
        # return result

        low , high ,res = 0 , len(s), []
        for ch in s:
            if ch == 'I':
                res.append(low)
                low += 1
            else:
                res.append(high)
                high -= 1
        res.append((low + high)//2) # middle
        return res