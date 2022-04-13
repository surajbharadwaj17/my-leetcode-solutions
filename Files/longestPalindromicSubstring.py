def longestPalindrone(s):
    
    def helper(s, l, r):
        while(l >= 0 and r < len(s) and s[l] == s[r]):
            print(l,r)
            l += 1
            r -= 1

        return s[l+1:r]

    ret = ""
    for i in range(len(s)):
        
        # odd case
        tmp = helper(s,i,i)
        if  len(tmp) > len(ret):
            ret = tmp

        # even case
        tmp = helper(s,i,i+1)
        if len(tmp) > len(ret):
            ret = tmp

    return ret


print(longestPalindrone("babad"))

        