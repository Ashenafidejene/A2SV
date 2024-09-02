-- Write your PostgreSQL query statement below
SELECT Customers.name As Customers FROM
 Customers LEFT JOIN 
 Orders ON Customers.id=Orders.customerId
 where Orders.customerId is Null ; 