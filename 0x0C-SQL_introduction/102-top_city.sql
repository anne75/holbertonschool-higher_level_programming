-- Display 3 highest average temperatures in July and August along with the city
-- Sort by temperatures in descending order
SELECT `city`, AVG(`value`) as avg_temp
FROM temperatures
WHERE `month` >= 7 and `month` <= 8
GROUP BY `city`
ORDER BY avg_temp DESC
LIMIT 3;
