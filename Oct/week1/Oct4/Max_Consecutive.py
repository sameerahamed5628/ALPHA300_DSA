class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        maax=0
        count=0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
                if count>maax:
                    maax=count
            else:
                count=0
        return maax