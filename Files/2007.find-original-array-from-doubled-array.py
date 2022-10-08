#
# @lc app=leetcode id=2007 lang=python3
#
# [2007] Find Original Array From Doubled Array
#

# @lc code=start


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        counter = collections.Counter(changed)

        if counter[0] %2:
            return []
        
        for key in sorted(counter):
            if counter[key] > counter[2*key]:
                return []
            counter[2*key] -= counter[key] if key else counter[key]//2
        print(counter)
        #return [key for key,val in counter.items() if val]
        return list(counter.elements())

        # c = collections.Counter(changed)
        # if c[0] % 2:
        #     return []
        # for x in sorted(c):
        #     if c[x] > c[2 * x]:
        #         return []
        #     c[2 * x] -= c[x] if x else c[x] // 2
        # return list(c.elements())
        
# @lc code=end

