WITH result AS (
    SELECT class, COUNT(*) AS students 
    FROM courses 
    GROUP BY class
)
SELECT class 
FROM result 
WHERE students >= 5;