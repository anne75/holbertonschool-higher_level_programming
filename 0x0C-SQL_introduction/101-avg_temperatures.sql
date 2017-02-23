-- Displays the average temperature by city
-- Sort by temperature descending
-- SELECT
-- city, AVG(`value`) AS avg_tmp
-- FROM temperatures
-- GROUP BY city
-- ORDER BY avg_tmp DESC;
-- Displays the average temperature by city (DESC)
SELECT
    city, AVG(value) AS avg_temp
    FROM temperatures
    GROUP BY city
    ORDER BY avg_temp DESC;
