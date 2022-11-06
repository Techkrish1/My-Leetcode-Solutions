class Solution:
    def fib(self, n: int) -> int:
        left  = 0
        right = 1
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            for i in range(2,n+1):
                temp = right
                right = left + right
                left = temp
            return right