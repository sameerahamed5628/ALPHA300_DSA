class Solution(object):
    def countSubstrings(self, s):
        count=0
        for mid in range(len(s)):
            start=mid
            end=mid
            while start>=0 and end<len(s) and s[start]==s[end]:
                count+=1
                start-=1
                end+=1
            
            start=mid
            end=mid+1
            while start>=0 and end<len(s) and s[start]==s[end]:
                count+=1
                start-=1
                end+=1
        return count