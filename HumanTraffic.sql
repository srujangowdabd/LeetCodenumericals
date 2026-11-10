# Write your MySQL query statement below
WITH consecutive AS (
    SELECT s1.id AS start_id
    FROM Stadium s1
    JOIN Stadium s2
        ON s2.id = s1.id + 1
    JOIN Stadium s3
        ON s3.id = s1.id + 2
    WHERE s1.people >= 100
      AND s2.people >= 100
      AND s3.people >= 100
)
SELECT DISTINCT s.*
FROM Stadium s
JOIN consecutive c
    ON s.id BETWEEN c.start_id AND c.start_id + 2
ORDER BY s.visit_date;
