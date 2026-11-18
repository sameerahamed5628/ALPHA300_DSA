class Solution(object):
    def reorganizeString(self, s):
        build={}
        for x in s:
            if x in build:
                build[x]+=1
            else:
                build[x]=1

        threshold=(len(s)+1)//2
        if max(build.values())>threshold:
            return ""
        
        new={}
        while build:
            maax=max(build,key=build.get)
            new[maax]=build[maax]
            del build[maax]

        out=[]
        while new:
            hold=None
            for z in new:
                if out and z==out[-1]:
                    continue
                if hold is None or new[z]>new[hold]:
                    hold=z
            out.append(hold)
            new[hold]-=1
            if new[hold]==0:
                del new[hold]
        return "".join(out)she