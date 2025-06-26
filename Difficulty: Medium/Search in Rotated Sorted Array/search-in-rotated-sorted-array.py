#User function Template for python3

class Solution:
    def search(self,arr,key):
        # Complete this function
        n=len(arr)
        low=0
        high=n-1
        while(low<=high):
            mid=(low+high)//2
            if(arr[mid]==key):
                return mid
            if(arr[low]<=arr[mid]):
                if(arr[low]<=key<=arr[mid]):
                    high=mid-1
                else:
                    low=mid+1
            elif(arr[mid]<=arr[high]):
                if(arr[mid]<=key<=arr[high]):
                    low=mid+1
                else:
                    high=mid-1
        return -1