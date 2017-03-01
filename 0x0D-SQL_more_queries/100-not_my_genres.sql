-- The db hbtn_0dtvshows is passed by argument
-- List all genres not linked to the tv show Dexter
-- only 2 S... statements


SELECT DISTINCT tv_genres.`name`
FROM tv_genres
WHERE tv_genres.id not in
      (SELECT DISTINCT t.genre_id
      FROM tv_show_genres t
      INNER JOIN tv_shows u ON u.id = t.show_id
      INNER JOIN tv_genres v ON t.genre_id = v.id
      WHERE u.`title` = 'Dexter')
ORDER BY tv_genres.`name` ASC

;
