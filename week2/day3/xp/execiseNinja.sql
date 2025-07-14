---Retrieve all G or PG rated films that are not currently rented

SELECT DISTINCT f.film_id, f.title, f.rating
FROM   film f
JOIN   inventory i ON f.film_id = i.film_id
LEFT JOIN rental r ON i.inventory_id = r.inventory_id
                   AND r.return_date IS NULL
WHERE  f.rating IN ('G', 'PG')
  AND  r.rental_id IS NULL;

-- 2. Create a waiting list table for kids' movies

CREATE TABLE kids_waiting_list (
    waiting_id SERIAL PRIMARY KEY,
    film_id INT REFERENCES film(film_id),
    child_name VARCHAR(100) NOT NULL,
    request_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
-- Test the waiting list – Add some test rows
INSERT INTO kids_waiting_list (film_id, child_name)
VALUES 
    (1, 'Sara'),
    (1, 'Omar'),
    (2, 'Youssef'),
    (3, 'Aya'),
    (3, 'Hana'),
    (3, 'Anas');
-- Retrieve number of children waiting per DVD
SELECT f.film_id,
       f.title,
       COUNT(k.waiting_id) AS number_waiting
FROM   film f
JOIN   kids_waiting_list k ON f.film_id = k.film_id
GROUP  BY f.film_id, f.title
ORDER  BY number_waiting DESC;
