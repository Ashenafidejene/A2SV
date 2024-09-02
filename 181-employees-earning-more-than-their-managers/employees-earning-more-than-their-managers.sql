-- Write your PostgreSQL query statement below
SELECT Employee.name as Employee
FROM Employee 
WHERE Employee.salary > (
    SELECT Manager.salary 
    FROM Employee AS Manager 
    WHERE Employee.managerId = Manager.id
);