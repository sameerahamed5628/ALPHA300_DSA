class Solution(object):
    def pivotIndex(self, nums):
        summ=0
        for i in range(len(nums)):
            if summ==sum(nums[i+1:]):
                return i
            summ+=nums[i]
        return -1
