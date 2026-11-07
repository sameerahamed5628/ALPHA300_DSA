class Solution(object):
    def capitalizeTitle(self, title):
        new=[]
        for x in range(len(title)):
            if 65<=ord(title[x]) and ord(title[x])<=90:
                n=ord(title[x])
                new.append(chr(n+32))
            else:
                new.append(title[x])
        new="".join(new)
        final=[]
        cut=new.split()
        for word in cut:
            if len(word)>=3:
                start=chr(ord(word[0])-32)
                full=start+word[1:]
                final.append(full)
            else:
                final.append(word)
        return " ".join(final)