-- import hbtn_0c_0 database this table dump: download
-- script that displays the average temperature by cty ordered by
-- temperature descending
SELECT city, AVG(value) as avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
