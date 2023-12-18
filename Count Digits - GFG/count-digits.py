#User function Template for python3


class Solution:
    def evenlyDivides (self, N):
        count = 0
        a = N
        while N != 0:
            e =  a % 10
            if e!=0 and N % e == 0:
                count += 1
            if a // 10 == 0:
                break
            a = a // 10
        return count
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.evenlyDivides(N))
# } Driver Code Ends