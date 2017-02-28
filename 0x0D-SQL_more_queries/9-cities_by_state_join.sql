-- In db passed by argument hbtn_0d_usa
-- List all cities and their state name in cities id ascending order
SELECT cities.`id`, cities.`name`, states.`name`
FROM cities
LEFT JOIN states ON cities.state_id = states.`id`
;
