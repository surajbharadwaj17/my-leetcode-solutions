/*
 * @lc app=leetcode id=137 lang=java
 *
 * [137] Single Number II
 */

// @lc code=start

import java.util.HashMap;

class Solution {
    public int singleNumber(int[] nums) {
        HashMap<Integer, Integer> hmap = new HashMap<>();

        for(int i=0; i<nums.length; i++) {
            if(hmap.containsKey(nums[i])){
                int count = hmap.get(nums[i]);
                hmap.put(nums[i], count+1);
            } else {
                hmap.put(nums[i], 1);
            }
        }

        for(int i : hmap.keySet()) {
            if (hmap.get(i)==1) {
                return i;
            }
        }
        return 0;
    }
}
// @lc code=end

