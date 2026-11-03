class Solution(object):
    def runningSum(self, nums):
        i=1
        while i!=len(nums):
            run=nums[i]+nums[i-1]
            nums[i]=run
            i+=1
        return nums