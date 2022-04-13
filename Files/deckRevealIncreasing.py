def deckRevealIncreasing(deck):
    deck = sorted(deck)
    left,right = 0,len(deck)-2
    #left_ret,right_ret = [],[]
    ret = []
    mid = len(deck)//2  -1 
    if left > right:
        return deck
    for left in range(0,mid):    
        ret.append(deck[left])
        if right > mid: 
            ret.append(deck[right])
            right -=1
    print(ret)
    print(left)
    print(right)
    ret.append(deck[-1])  
    #if len(deck)%2 !=0:
    ret.append(deck[right])
    
    return ret

deck = [1,2,3,4]
deck2 = [17,13,11,2,3,5,7]

#deck1 answer = [1,3,2,4]
# deck2 Expected:
# [2,13,3,11,5,17,7]
print(deckRevealIncreasing(deck))