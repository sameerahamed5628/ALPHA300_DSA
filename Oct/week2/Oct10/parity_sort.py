class Solution(object):
    def sortArrayByParity(self, nums):
        even=[]
        odd=[]
        for x in nums:
            if x%2==0:
                even.append(x)
            else:
                odd.append(x)
        even.extend(odd)
        return even
        