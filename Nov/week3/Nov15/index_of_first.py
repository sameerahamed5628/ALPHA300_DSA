class Solution(object):
    def strStr(self, haystack, needle):
        m=len(haystack)
        n=len(needle)
        for i in range(m-n+1):
            check=True
            for j in range(n):
                if haystack[i+j]!=needle[j]:
                    check=False
                    break
            if check==True:
                return i
        return -1