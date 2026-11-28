class Solution(object):
    def totalFruit(self, fruits):
        basket={}
        left=0
        take=0
        
        for right in range(len(fruits)):
            fruit=fruits[right]
            if fruit in basket:
                basket[fruit]+=1
            else:
                basket[fruit]=1
            
            while len(basket)>2:
                extra=fruits[left]
                basket[extra]-=1
                if basket[extra]==0:
                    del basket[extra]
                left+=1
            take=max(take,right-left+1)
        return take