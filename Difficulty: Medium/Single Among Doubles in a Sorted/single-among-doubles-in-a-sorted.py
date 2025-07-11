class Solution:
    def findOnce(self,arr):
        n=len(arr)
        if(n==1):
            return arr[0]
        elif(arr[0]!=arr[1]):
            return arr[0]
        elif(arr[n-1]!=arr[n-2]):
            return arr[n-1]
        low=1
        high=n-2
        while(low<=high):
            mid=(low+high)//2
            if(arr[mid]!=arr[mid-1] and arr[mid]!=arr[mid+1]):
                return arr[mid]
            elif((mid%2==1 and arr[mid]==arr[mid-1]) or (mid%2==0 and arr[mid]==arr[mid+1])):
                low=mid+1
            elif((mid%2==0 and arr[mid]==arr[mid-1]) or (mid%2==1 and arr[mid]==arr[mid+1])):
                high=mid-1
        