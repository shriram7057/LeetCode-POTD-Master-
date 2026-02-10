SELECT e.employee_id
FROM Employees e
LEFT JOIN Employees m
    ON e.manager_id = m.employee_id
WHERE e.manager_id IS NOT NULL
  AND m.employee_id IS NULL
  AND e.salary < 30000
ORDER BY e.employee_id ASC;
