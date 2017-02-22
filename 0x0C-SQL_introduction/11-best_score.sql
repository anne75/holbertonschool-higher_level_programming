-- Select only the best scores
SELECT `score`, `name`
FROM second_table
WHERE `score` >= 10
ORDER BY `score` desc;
