class Solution:

    def reverseInGroups(self, arr, k):
        for x in range(0,len(arr),k):
            left=x
            if x+(k-1)>len(arr)-1:
                right=len(arr)-1
            else:
                right=x+(k-1)
        
            while left<right:
                arr[left],arr[right]=arr[right],arr[left]
                left+=1
                right-=1
        return arr