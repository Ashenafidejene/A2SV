CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
  RETURN QUERY (
    -- Write your PostgreSQL query statement below.
with SingleValue As(
    SELECT 
    Employee.salary AS salary
    from Employee
    GROUP BY Employee.salary
),
RankEmployee AS(
    SELECT 
    SingleValue.salary As SecondHighestSalary,
    DENSE_RANK() OVER (ORDER BY SingleValue.salary DESC) As rank 
    from SingleValue
)
SELECT 
    CASE 
        WHEN EXISTS (SELECT 1 FROM RankEmployee WHERE rank = N) 
        THEN (SELECT SecondHighestSalary FROM RankEmployee WHERE rank = N)
        ELSE NULL 
    END AS SecondHighestSalary
      
  );
END;
$$ LANGUAGE plpgsql;