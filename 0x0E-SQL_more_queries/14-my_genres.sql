-- Script that uses the hbtn_0d_tvshows database to lists
-- all genres of the show
SELECT tv_genres.name
FROM tv_genres
LEFT JOIN tv_show_genres
ON tv_show_genres.genre_id = tv_genres.id
LEFT JOIN tv_shows
ON  tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'DEXTER'
ORDER BY tv_genres.name ASC;
