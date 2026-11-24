class Solution(object):
    def shortestPalindrome(self, s):
        n=0
        for mid in range(len(s)):
            start=mid
            end=mid
            while start>=0 and end<len(s) and s[start]==s[end]:
                start-=1
                end+=1
            if start==-1 and end>n:
                n=end
            
            start=mid
            end=mid+1
            while start>=0 and end<len(s) and s[start]==s[end]:
                start-=1
                end+=1
            if start==-1 and end>n:
                n=end

        out=""
        for i in range(len(s)-1,n-1,-1):
            out+=s[i]
        for i in range(len(s)):
            out+=s[i]
        return out
        