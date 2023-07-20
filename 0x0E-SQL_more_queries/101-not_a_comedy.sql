-- script that lists all shows without a genre comedy in the database hbtn_0d_tvshows.
SELECT tv_shows.title
FROM tv_shows
LEFT JOIN (
    SELECT show_id
    FROM tv_show_genres
    JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
    WHERE tv_genres.name = 'Comedy'
) AS comedy_shows ON tv_shows.id = comedy_shows.show_id
WHERE comedy_shows.show_id IS NULL
ORDER BY tv_shows.title;
