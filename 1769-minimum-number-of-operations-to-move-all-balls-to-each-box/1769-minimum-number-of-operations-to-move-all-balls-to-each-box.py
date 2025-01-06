class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans = [0] * n

        count,operation = 0,0
        for i in range(n):
            ans[i] = ans[i] + operation
            count = count + int(boxes[i])
            operation = operation + count

        # print(ans)
        # print(count,operation)
        count,operation = 0,0

        for i in range(n-1,-1,-1):
            ans[i] = ans[i] + operation
            count = count + int(boxes[i])
            operation = operation + count

        # print(ans)
        # print(count,operation)
        return ans