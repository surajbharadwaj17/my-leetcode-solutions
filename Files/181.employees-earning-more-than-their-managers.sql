--
-- @lc app=leetcode id=181 lang=mysql
--
-- [181] Employees Earning More Than Their Managers
--

-- @lc code=start
# Write your MySQL query statement below

SELECT E1.name as Employee
FROM Employee as E1, Employee as E2
WHERE E1.managerId = E2.id and E1.salary > E2.salary;

-- @lc code=end

