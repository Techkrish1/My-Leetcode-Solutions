class Solution:
    def fib(self, n: int) -> int:
        return self.fibn(n, {})
    
    
    def fibn(self, n, memo):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        if n not in memo:
            memo[n] = self.fibn(n-1, memo) + self.fibn(n-2, memo)
            
            
        return memo[n]
