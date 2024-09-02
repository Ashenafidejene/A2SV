-- Write your PostgreSQL query statement below
SELECT Customer.name as name 
from Customer
where Customer.referee_id != 2 or Customer.referee_id is NULL ;