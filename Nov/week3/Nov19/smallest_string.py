class Solution(object):
    def isAlienSorted(self, words, order):
        build={}
        n=0
        for x in order:
            build[x]=n
            n+=1
        for y in range(len(words)-1):
            now=words[y]
            nextt=words[y+1]
            for z in range(len(now)):
                if z==len(nextt):
                    return False
                if now[z]!=nextt[z]:
                    if build[now[z]]>build[nextt[z]]:
                        return False
                    break
        return True