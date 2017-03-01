-- Use the database hbtn_0d_tvshowsrate containing 4 tables
-- List all genres by decreasing order of popularity


SELECT tv_genres.`name`, SUM(tv_show_ratings.rate) AS 'rating'
FROM tv_genres
LEFT OUTER JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
LEFT OUTER JOIN tv_show_ratings ON tv_show_ratings.show_id = tv_show_genres.show_id
GROUP BY tv_genres.`name`
ORDER BY rating DESC
;
