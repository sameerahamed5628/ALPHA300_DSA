class Solution(object):
    def countAndSay(self, n):
        RLE="1"
        for x in range(n-1):
            new=[]
            count=1
            for i in range(1,len(RLE)):
                if RLE[i]==RLE[i-1]:
                    count+=1
                else:
                    new.append(str(count))
                    new.append(RLE[i-1])
                    count=1
            new.append(str(count))
            new.append(RLE[-1])
            RLE= "".join(new)
        return RLE