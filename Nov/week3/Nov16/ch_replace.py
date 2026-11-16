class Solution(object):
    def characterReplacement(self, s, k):
        doop={}
        left=0
        count=0
        for right in range(len(s)):
            x=s[right]
            if x in doop:
                doop[x]+=1
            else:
                doop[x]=1

            if doop[x]>count:
                count=doop[x]

            if (right-left+1)-count>k:
                doop[s[left]]-=1
                left+=1

        return len(s)-left

