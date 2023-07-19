-- script that displays the max temperature of each state
-- ordered by the state name
SELECT State, MAX(Temperature) AS Max_Temperature
FROM table_name
GROUP BY State
ORDER BY State;
