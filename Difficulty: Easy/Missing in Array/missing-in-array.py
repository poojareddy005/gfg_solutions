class Solution:
    def missingNum(self, arr):
        n=len(arr)+1
        total_sum=n*(n+1)//2
        arr_sum=sum(arr)
        missing_element=total_sum-arr_sum
        return missing_element


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    arr = list(map(int, input().split()))
    s = Solution().missingNum(arr)
    print(s)

    print("~")
# } Driver Code Ends