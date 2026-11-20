class Solution(object):
    def minWindow(self, s, t):
        if len(s)<len(t):
            return ""
        
        text={}
        for x in t:
            if x in text:
                text[x]+=1
            else:
                text[x]=1

        build={}
        maatch=0
        limit=len(text)

        left=0
        maax=float('inf')
        start=0

        for right in range(len(s)):
            y=s[right]
            if y in build:
                build[y]+=1
            else:
                build[y]=1
            if y in text and build[y]==text[y]:
                maatch+=1
            
            while maatch==limit:
                if right-left+1<maax:
                    maax=right-left+1
                    start=left
                back=s[left]
                build[back]-=1
                if back in text and build[back]<text[back]:
                    maatch-=1
                left+=1
        if maax==float('inf'):
            return ""
        return s[start:start+maax]