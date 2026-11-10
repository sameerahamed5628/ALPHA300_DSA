class Solution:
    def maxSubarraySum(self, arr, k):
        count=sum(arr[0:k])
        maax=count
        for i in range(k,len(arr)):
            count=count+arr[i]-arr[i-k]
            maax=max(count,maax)
        return maax