class Solution(object):
    def findMaxAverage(self, nums, k):
        count=sum(nums[0:k])
        maax=count
        for i in range(k,len(nums)):
            count=count+nums[i]-nums[i-k]
            maax=max(maax,count)
        return maax/float(k)
                       