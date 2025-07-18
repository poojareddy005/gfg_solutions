class Solution:
    def findKRotation(self, arr):
        n=len(arr)
        low=0
        high=n-1
        Min=float("inf")
        mIndex=-1
        while(low<=high):
            mid=(low+high)//2
            if(arr[low]<=arr[mid]):
                if(arr[low]<Min):
                    Min=arr[low]
                    mIndex=low
                low=mid+1
            if(arr[mid]<=arr[high]):
                if(arr[mid]<Min):
                    Min=arr[mid]
                    mIndex=mid
                high=mid-1
        return mIndex