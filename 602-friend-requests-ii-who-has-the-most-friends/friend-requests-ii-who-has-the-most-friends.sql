WITH requester AS (
    SELECT requester_id, COUNT(*) AS numberTotal
    FROM RequestAccepted
    GROUP BY requester_id
),
accepter AS (
    SELECT accepter_id, COUNT(*) AS number
    FROM RequestAccepted
    GROUP BY accepter_id
),
total AS (
    SELECT COALESCE(requester_id, accepter_id) AS user_id, 
           COALESCE(numberTotal, 0) + COALESCE(number, 0) AS maxs
    FROM requester
    FULL OUTER JOIN accepter ON requester.requester_id = accepter.accepter_id
)
SELECT  user_id as id , maxs as num
FROM total
ORDER BY maxs DESC
LIMIT 1;