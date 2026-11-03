class Solution(object):
    def findDisappearedNumbers(self, nums):
        n=len(nums)+1
        distinct={}
        for num in nums:
            distinct[num]=True
        new=[]
        for i in range(1,n):
            if i not in distinct:
                new.append(i)
        return new
        