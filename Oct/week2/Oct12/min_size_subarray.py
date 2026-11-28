class Solution(object):
    def minSubArrayLen(self, target, nums):
        minn=len(nums)+1
        start=0
        summ=0
        for i in range(len(nums)):
            summ+=nums[i]
            while summ>=target:
                minn=min(minn,i-start+1)
                summ-=nums[start]
                start+=1
                
        if minn==len(nums)+1:
            return 0
        return minn