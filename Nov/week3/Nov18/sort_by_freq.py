class Solution(object):
    def frequencySort(self, s):
        build={}
        for x in s:
            if x in build:
                build[x]+=1
            else:
                build[x]=1
        out=[]
        for hi in range(len(build)):
            n=max(build,key=build.get)
            x=build[n]
            for bye in range(x):
                out.append(n)
            del build[n]
        return "".join(out)
    