-- In db passed by argument hbtn_od_tvshows
-- List all show titles and their genres.
-- Do not include titles withour genres.

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_show_genres
INNER JOIN tv_shows on tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id
;
