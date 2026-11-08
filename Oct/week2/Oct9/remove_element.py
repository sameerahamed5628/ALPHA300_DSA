class Solution(object):
    def removeElement(self, nums, val):
        for i in range(len(nums)):
            if nums[i]==val:
                j=i+1
                while j!=len(nums):
                    if nums[i]==nums[j]:
                        j+=1
                    else:
                        nums[i],nums[j]=nums[j],nums[i]
                        i+=1
            else:
                i+=1
        count=0
        for x in nums:
            if x!=val:
                count+=1
        return count