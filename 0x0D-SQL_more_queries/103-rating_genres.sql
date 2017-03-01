-- Use the database hbtn_0d_tvshowsrate containing 4 tables
-- List all genres by decreasing order of popularity


SELECT tv_genres.name, b.rating
FROM tv_genres
INNER JOIN (
      SELECT tv_show_genres.genre_id AS a, SUM(tv_show_ratings.rate) AS 'rating'
      FROM tv_show_genres
      INNER JOIN tv_show_ratings ON tv_show_ratings.show_id = tv_show_genres.show_id
      GROUP BY tv_show_genres.genre_id) AS b
ON tv_genres.id = b.a
ORDER BY b.rating DESC
;
