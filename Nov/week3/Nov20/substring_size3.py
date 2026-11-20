class Solution(object):
    def countGoodSubstrings(self, s):
        left=0
        count=0
        while left<=len(s)-3:
            build={}
            for x in range(left,left+3):
                if s[x] in build:
                    build[s[x]]+=1
                else:
                    build[s[x]]=1
            if len(build)==3:
                count+=1
            left+=1
        return count
        