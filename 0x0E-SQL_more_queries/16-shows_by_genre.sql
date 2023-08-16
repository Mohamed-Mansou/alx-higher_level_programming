-- SQL lists all shows and linked genres from the database hbtn_0d_tvshows
SELECT title, tv_genres.name FROM tv_shows
LEFT JOIN tv_show_genres ON id=tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY title, tv_genres.name;
