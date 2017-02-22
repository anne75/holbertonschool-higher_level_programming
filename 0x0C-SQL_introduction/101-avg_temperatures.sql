-- Displays the average temperature by city
-- Sort by temperature descending
SELECT `city`, AVG(`value`) as `avg_tmp`
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_tmp` DESC;
