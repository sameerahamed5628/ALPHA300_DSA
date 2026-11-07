class Solution(object):
    def defangIPaddr(self, address):
        new=[]
        for x in range(len(address)):
            if address[x]== ".":
                new.append("[.]")
            else:
                new.append(address[x])

        return "".join(new)
        