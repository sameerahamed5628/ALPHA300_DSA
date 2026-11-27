class Solution(object):
    def rearrangeCharacters(self, s, target):
        build={}
        for x in target:
            build[x]=build.get(x,0)+1
        doop={}
        for x in s:
            doop[x]=doop.get(x,0)+1
        count=('inf')
        for x in build:
            count=min(count,doop.get(x,0)//build.get(x,0))
        return count
 