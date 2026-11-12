class Solution(object):
    def compress(self, chars):
        place=0
        i=0
        while i<len(chars):
            s=chars[i]
            count=0
            while i<len(chars) and chars[i]==s:
                count+=1
                i+=1
            chars[place]=s
            place+=1
            if count>1:
                for x in str(count):
                    chars[place]=x
                    place+=1
        return place
            