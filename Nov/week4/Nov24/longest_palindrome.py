class Solution(object):
    def longestPalindrome(self, s):
        longest=""
        for mid in range(len(s)):
            start=mid
            end=mid
            while start>=0 and end<len(s) and s[start]==s[end]:
                start-=1
                end+=1
            if end-start-1>len(longest):
                longest=""
                for i in range(start+1,end):
                    longest+=s[i]
            
            start=mid
            end=mid+1
            while start>=0 and end<len(s) and s[start]==s[end]:
                start-=1
                end+=1
            if end-start-1>len(longest):
                longest=""
                for i in range(start+1,end):
                    longest+=s[i]
        return longest