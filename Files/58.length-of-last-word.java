/*
 * @lc app=leetcode id=58 lang=java
 *
 * [58] Length of Last Word
 */

// @lc code=start
class Solution {
    public int lengthOfLastWord(String s) {
        String[] aStrings = s.split(" ");
        return aStrings[aStrings.length-1].length();
    }
}
// @lc code=end

