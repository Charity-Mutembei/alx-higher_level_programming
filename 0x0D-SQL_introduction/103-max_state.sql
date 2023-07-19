-- script that displays the max temperature of each state
-- ordered by the state name.
SELECT State, MAX(value) AS Max_Temperature
FROM temperatures
GROUP BY State
ORDER BY State;
