#User function Template for python3


class Solution:
    def missingNumber(self,array,n):
        # code here
        res = [0]*n
        for i in range(1,n):
            res[array[i-1]-1] = 1
        return res.index(0) + 1

#{ 
 # Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().missingNumber(a,n)
    print(s)
# } Driver Code Ends