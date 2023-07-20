-- script that uses the hbtn_0d+tvshows database to list all genres not linked to the show Dexter. 
SELECT tv_genres.name
FROM tv_genres
LEFT JOIN (
    SELECT genre_id
    FROM tv_show_genres
    JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
    WHERE tv_shows.title = 'Dexter'
) AS linked_genres ON tv_genres.id = linked_genres.genre_id
WHERE linked_genres.genre_id IS NULL
ORDER BY tv_genres.name;
