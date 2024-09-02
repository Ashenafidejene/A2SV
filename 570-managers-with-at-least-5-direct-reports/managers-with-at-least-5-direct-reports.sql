-- Write your PostgreSQL query statement below
WITH manager AS (
    SELECT 
        Employee.managerId AS id
    FROM 
        Employee
    GROUP BY 
        Employee.managerId
    HAVING COUNT(*) >= 5
)
SELECT  
    Employee.name AS name
FROM 
    Employee 
JOIN
    manager 
ON 
    manager.id = Employee.id
;

        
    
