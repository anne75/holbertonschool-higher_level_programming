-- List records with a name value.
-- Sort by score in descending order
SELECT `score`, `name`
FROM second_table
WHERE `name` IS NOT NULL
ORDER BY `score` DESC;
