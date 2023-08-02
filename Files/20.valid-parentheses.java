/*
 * @lc app=leetcode id=20 lang=java
 *
 * [20] Valid Parentheses
 */

// @lc code=start

import java.util.ArrayList;

class Solution {
    public boolean isValid(String s) {

        if (s.length()%2 == 1) {
            return false;
        }

        ArrayList<Character> stack = new ArrayList<>();

        for(int i=0; i < s.length(); i++) {
            if (s.charAt(i) == '{' || s.charAt(i) == '[' || s.charAt(i) == '(') {
                stack.add(s.charAt(i));
            } else {
                if (stack.size() == 0) {
                    return false;
                }          
                if ((stack.get(stack.size()-1) == '{' && s.charAt(i) == '}')
                || (stack.get(stack.size()-1) == '[' && s.charAt(i) == ']' )
                || (stack.get(stack.size()-1) == '(' && s.charAt(i) == ')')) {
                    stack.remove(stack.size()-1);
                } else {
                    return false;
                }
            }
        }

        if (stack.size() > 0) {
            return false;
        } else {
            return true;
        }
    }
}
// @lc code=end

