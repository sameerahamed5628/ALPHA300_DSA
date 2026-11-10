class Solution(object):
    def trimMean(self, arr):
        arr.sort()
        m=len(arr)//20
        n=len(arr)-m
        add=0
        count=0
        for i in range(m,n):
            add+=arr[i]
            count+=1
        mean=float(add)/count
        return mean
        