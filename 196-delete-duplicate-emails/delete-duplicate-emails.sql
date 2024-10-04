-- Write your PostgreSQL query statement below
WITH CTE AS (
  SELECT id,
         ROW_NUMBER() OVER (PARTITION BY email ORDER BY id) AS rn
  FROM person 
)
DELETE FROM person
WHERE id IN (
  SELECT id
  FROM CTE
  WHERE rn > 1
);