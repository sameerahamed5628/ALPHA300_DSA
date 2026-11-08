class Solution(object):
    def sortedSquares(self, nums):
        new=[]
        for x in nums:
            s=x*x
            new.append(s)
        new.sort()
        return new
        