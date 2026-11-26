class Solution(object):
    def maxPower(self, s):
        maxx=1
        count=1
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                count+=1
            else:
                maxx=max(count,maxx)
                count=1
            maxx=max(count,maxx)
        return maxx