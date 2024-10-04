WITH CTE AS (
  SELECT customer_number,
         ROW_NUMBER() OVER (PARTITION BY customer_number ORDER BY order_number) AS rn
  FROM Orders
),
rankcustomer AS (
  SELECT CTE.customer_number,
         DENSE_RANK() OVER (ORDER BY rn DESC) AS rank
  FROM CTE
)
SELECT rankcustomer.customer_number 
FROM rankcustomer 
WHERE rank = 1;