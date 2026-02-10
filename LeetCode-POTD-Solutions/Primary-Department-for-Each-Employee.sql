# Write your MySQL query statement below
SELECT 
    employee_id,
    department_id
FROM Employee
WHERE primary_flag = 'Y'
UNION
SELECT 
    employee_id,
    MIN(department_id)
FROM Employee
GROUP BY employee_id
HAVING SUM(primary_flag = 'Y') = 0;
