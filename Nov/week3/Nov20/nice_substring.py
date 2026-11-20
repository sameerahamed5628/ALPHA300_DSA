class Solution(object):
    def longestNiceSubstring(self, s):
        out=""
        for i in range(len(s)):
            for j in range(i,len(s)):
                sub=s[i:j+1]
                nice=True

                for x in sub:
                    if x.swapcase() not in sub:
                        nice=False
                        break
                if nice and len(sub)>len(out):
                    out=sub
        return out