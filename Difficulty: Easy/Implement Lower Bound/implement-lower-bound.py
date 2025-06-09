#User function Template for python3
class Solution:
    def lowerBound(self, arr, target):
        n=len(arr)
        low=0
        high=n-1
        ans=n
        while(low<=high):
            mid=(low+high)//2
            if(arr[mid]>=target):
                high=mid-1
                ans=mid
            elif(arr[mid]<target):
                low=mid+1
        return ans