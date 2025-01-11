class Solution:
    def fib(self, n: int) -> int:
        # recursive way
        # if n <= 1:
        #     return n
        # return  self.fib(n-1) + self.fib(n-2)

        # iterative way
        if n <= 1:
            return n
        a,b = 0,1
        for _ in range(2,n+1):
            a,b = b , a+b
        return b