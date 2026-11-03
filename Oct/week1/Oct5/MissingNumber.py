class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)+1
        new=[]
        for i in range(n):
            new.append(i)
        for num in nums:
            if num in new:
                new.remove(num)
        return new[0]
        