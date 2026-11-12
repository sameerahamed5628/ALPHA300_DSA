class Solution:

    def encode(self, strs:str):
        ec=""
        for word in strs:
            ec+=str(len(word))+"#"+word
        return ec

    def decode(self, s: str):
        output=[]
        i=0
        while i<len(s):
            size=""
            while s[i]!="#":
                size+=s[i]
                i+=1
            length=int(size)
            i+=1
            new=""
            for x in range(length):
                new+=s[i]
                i+=1
            output.append(new)
        return output
        