class Solution(object):
    def countHomogenous(self, s):
        homo=0
        count=0
        for i in range(len(s)):
            if i>0 and s[i]==s[i-1]:
                count+=1
            else:
                count=1
            homo+=count
        return homo % (10**9+7)
