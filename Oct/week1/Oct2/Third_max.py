class Solution(object):
    def thirdMax(self, nums):
        i=0
        while i<len(nums)-1:
            j=i+1
            while j<len(nums):
                if nums[i]<nums[j]:
                    nums[i],nums[j]=nums[j],nums[i]
                j+=1
            i+=1
        maax=nums[0]
        k=0
        count=1
        while k<len(nums):
            if count!=3:
                if nums[k]!=maax:
                    maax=nums[k]
                    count+=1
            k+=1
        if count<3:
            return nums[0]
        return maax