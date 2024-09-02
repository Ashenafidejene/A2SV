-- Write your PostgreSQL query statement below
SELECT Scores.score , DENSE_RANK() OVER(ORDER BY Scores.score DESC)  AS rank FROM Scores;