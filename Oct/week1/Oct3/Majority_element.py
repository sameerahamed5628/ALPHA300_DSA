class Solution(object):
    def majorityElement(self, nums):
        if not nums:
            return []
        nums.sort()
        maj=0
        n=len(nums)/2
        i=0
        count=1
        while i<len(nums)-1:
            if nums[i]==nums[i+1]:
                count+=1
            else:
                if count>n:
                    maj=nums[i]
                count=1
            i+=1
        if count>n:
            maj=nums[len(nums)-1]
        return maj