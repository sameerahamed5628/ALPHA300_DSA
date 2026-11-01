class Solution(object):
    def singleNumber(self, nums):
        if len(nums)<2:
            return nums[0]
        nums.sort()
        x=0
        while x<len(nums)-1:
            if nums[x]==nums[x+1]:
                x+=2
            else:
                return nums[x]
        return nums[-1]