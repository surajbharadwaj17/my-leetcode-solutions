/*
 * @lc app=leetcode id=9 lang=java
 *
 * [9] Palindrome Number
 */

// @lc code=start
class Solution {
    public boolean isPalindrome(int x) {
        String xStr = Integer.toString(x);
        int n = xStr.length();
        int left = 0;
        int right = n-1;

        while (left < right) {
            if (xStr.charAt(left) != xStr.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }

        return true;
    }
}
// @lc code=end

