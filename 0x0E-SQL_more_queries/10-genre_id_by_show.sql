-- script that lists all shows contained in hbtn_0d_tvshows
SELECT tv_shows.title, tv_shows_genres.genre_id FROM tv_shows INNER JOIN tv_shows_genres ON tv_shows.id=tv_shows_genres.shows_id ORDER BY tv_shows.title, tv_shows_genres.genre_id ASC;
