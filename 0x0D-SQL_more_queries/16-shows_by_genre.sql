-- The db is passed by argument, use hbtn_0dtvshows
-- List all shows and the genre names associated to that show

SELECT tv_shows.title, tv_genres.`name`
FROM tv_genres
RIGHT OUTER JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
RIGHT OUTER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title ASC

;

-- To add all genres without shows
-- UNION
-- FROM tv_genres
-- LEFT OUTER JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
-- LEFT OUTER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
-- UNION
-- SELECT *
