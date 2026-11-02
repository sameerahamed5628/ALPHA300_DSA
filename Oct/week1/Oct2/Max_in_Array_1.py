class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maax=0
        x=0
        while x<len(candies):
            if candies[x]>maax:
                maax=candies[x]
            x+=1
        output=[]
        y=0
        while y<len(candies):
            if candies[y]+extraCandies>=maax:
                output.append(True)
            else:
                output.append(False)
            y+=1
        return output