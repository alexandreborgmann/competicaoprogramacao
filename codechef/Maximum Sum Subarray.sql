SELECT MAX(max_subarray_sum) AS "Max Subarray Sum"
FROM (
    SELECT 
        a.key1 AS start_key, 
        b.key1 AS end_key, 
        SUM(c.val1) AS max_subarray_sum
    FROM ArrayTable a
    JOIN ArrayTable b ON a.key1 <= b.key1
    JOIN ArrayTable c ON c.key1 BETWEEN a.key1 AND b.key1
    GROUP BY a.key1, b.key1
) AS subarray_sums;


WITH RECURSIVE SubarraySums AS (
  SELECT key1, val1, val1 AS max_sum
  FROM ArrayTable
  WHERE key1 = 1
  UNION ALL
  SELECT t.key1, t.val1, 
         CASE WHEN s.max_sum + t.val1 > t.val1 THEN s.max_sum + t.val1 ELSE t.val1 END AS max_sum
  FROM ArrayTable AS t
  JOIN SubarraySums AS s ON t.key1 = s.key1 + 1
)
SELECT MAX(max_sum) AS "Max Subarray Sum"
FROM SubarraySums;