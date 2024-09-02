-- Write your PostgreSQL query statement below
SELECT Person.email as Email fROM  Person GROUP BY Person.email HAVING count(*) > 1;