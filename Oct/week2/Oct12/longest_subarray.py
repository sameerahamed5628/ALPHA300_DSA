class Solution:
    def longestSubarray(self, arr, k):
        indexx={0:-1}
        total=0
        longg=0
        for i in range(len(arr)):
            total+=arr[i]
            if total-k in indexx:
                longg=max(longg,i-indexx[total-k])
            if total not in indexx:
                indexx[total]=i
        return longg