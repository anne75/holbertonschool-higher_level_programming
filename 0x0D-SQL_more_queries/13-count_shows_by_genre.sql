-- In db passed by argument hbtn_od_tvshows
-- List all genres and the number of times they are referenced
-- Use only one S clause

SELECT tv_genres.`name`, COUNT(tv_show_genres.genre_id) AS 'number_shows'
FROM tv_show_genres
INNER JOIN tv_genres on tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.`name`
ORDER BY 2 DESC
;
