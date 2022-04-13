## BACKTRACKING ##

def rangeToList(k):
    return [str(i) for i in range(k)]

def baseKStrings(n,k):
    # base case
    if n == 0:
        return []
    
    if n == 1:
        return rangeToList(k)

    # recursive case
    result = []
    for i in rangeToList(k):
        for j in baseKStrings(n-1,k):
            result.append(i+j)
    return result

print(baseKStrings(4,5))
