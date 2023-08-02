/*
 * @lc app=leetcode id=66 lang=java
 *
 * [66] Plus One
 */

// @lc code=start
class Solution {
    public int[] plusOne(int[] digits) {
        int num = Integer.valueOf(digits.toString());
        num++;
        String sDString = Integer.toString(num);
        String[] aStrings = sDString.split("");
        int[] ret = null;
        for (String s:aStrings) {
            System.out.println(s);
        }
        return ret;
    }
}
// @lc code=end

