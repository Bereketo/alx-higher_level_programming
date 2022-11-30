-- lists all cities contained in the database hbtn_0d_usa
--  display: cities.id - cities.name - states.name
SELECT c.id, c.name, s.name
FROM states s
INNER JOIN cities c
ON s.id = c.state_id ORDER BY(c.id) ASC;
