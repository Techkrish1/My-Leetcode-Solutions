class Solution:
    def thirdLargest(self,a, n):
        # code here
        if len(a) < 3:
            return -1
            
        first = float('-inf')
        second = float('-inf')
        third = float('-inf')
        
        for i in a:
            if i > first:
                first, second, third = i, first,second
            elif i > second:
                second , third = i, second
            elif i > third:
                third = i
        
        return third
            


#{ 
 # Driver Code Starts
# Your code goes here
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(Solution().thirdLargest(arr, n))
# } Driver Code Ends