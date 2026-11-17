#35/38 TEST CASES PASSED
#My First HARD question in LEETCODE
#This is my own code build from scratch which faces TLE,finding hard to retify or understand the solution
#Hoping to fully complete Hard Problems in upcoming sessions
class Solution(object):
    def sumPrefixScores(self, words):
        slicer=max(words,key=len)
        build={}
        for x in range(1,len(slicer)+1):
            for word in words:
                if len(word)>=x:
                    hi=word[:x]
                    build[hi]=build.get(hi,0)+1
        out=[]
        for word in words:
            cut=len(word)
            score=0
            for y in range(1,cut+1):
                bye=word[:y]
                score+=build[bye]
            out.append(score)
        return out