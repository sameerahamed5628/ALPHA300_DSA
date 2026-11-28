class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        new=sentence.split(" ")
        n=len(searchWord)
        for x in range(len(new)):
            w=new[x]
            if len(w)<n:
                continue
            i=0
            while i<n and w[i]==searchWord[i]:
                i+=1
            if i==n:
                return x+1
        return -1