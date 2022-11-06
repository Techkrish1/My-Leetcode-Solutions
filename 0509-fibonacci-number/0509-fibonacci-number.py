class Solution:
    def fib(self, n: int) -> int:
        dp_0,dp_1 = 0,1
        for i in range(n):
            dp_0,dp_1 = dp_1,dp_1+dp_0
        return dp_0