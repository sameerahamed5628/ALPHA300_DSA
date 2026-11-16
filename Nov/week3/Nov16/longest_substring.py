class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left=0
        maxx=0
        doop=[]
        for i in range(len(s)):
            while s[i] in doop:
                doop.remove(s[left])
                left+=1
            doop.append(s[i])
            maxx=max(maxx,i-left+1)
        return maxx  