-- The db is passed by argument, use hbtn_0dtvshows
-- List all tv shows that are not Comedies

SELECT tv_shows.title
FROM tv_shows
WHERE tv_shows.title not in (
      SELECT tv_shows.title
      FROM tv_genres
      INNER JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
      INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
      WHERE tv_genres.`name` = 'Comedy')
ORDER BY tv_shows.title ASC
;
