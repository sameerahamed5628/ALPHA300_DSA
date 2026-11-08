class Solution(object):
    def moveZeroes(self, nums):
        for i in range(len(nums)-1):
            j=i+1
            if nums[i]==0:
                while j!=range(len(nums)):
                    if nums[j]==0:
                        j+=1
                    else:
                        nums[i],nums[j]=nums[j],nums[i]
                        i+=1
                        j+=1
            else:
                i+=1   
        return nums
                
        