class Solution(object):
    def firstUniqChar(self, s):
        times={}
        for x in s:
            if x in times:
                times[x]+=1
            else:
                times[x]=1
        for y in range(len(s)):
            if times[s[y]]==1:
                return y
        return -1
        