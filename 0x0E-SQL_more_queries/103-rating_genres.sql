-- script that lists all generes in the database
SELECT tv_genres.name, SUM(hbtn_0d_tvshows_rate.rating) AS rating_sum
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN hbtn_0d_tvshows_rate ON tv_show_genres.show_id = hbtn_0d_tvshows_rate.show_id
GROUP BY tv_genres.id, tv_genres.name
ORDER BY rating_sum DESC;
