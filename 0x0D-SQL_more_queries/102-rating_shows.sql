-- Use the database hbtn_0d_tvshows_rate
-- List all shows and their ratings by popularity decreasing

SELECT tv_shows.title, SUM(tv_show_ratings.rate) as 'rating'
FROM tv_shows
INNER JOIN tv_show_ratings ON tv_show_ratings.show_id = tv_shows.id
GROUP BY tv_shows.title
ORDER BY rating DESC
;
