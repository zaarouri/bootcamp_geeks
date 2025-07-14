-- EXERCISE 1 -----------------------------------------------

-- 1. Get all languages
SELECT * FROM language;

-- 2. Films joined with their languages
SELECT f.title, f.description, l.name AS language
FROM film f
JOIN language l ON f.language_id = l.language_id;

-- 3. All languages even if no films
SELECT f.title, f.description, l.name AS language
FROM language l
LEFT JOIN film f ON f.language_id = l.language_id;

-- 4. Create new_film table
CREATE TABLE IF NOT EXISTS new_film (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- Add some films
INSERT INTO new_film (name)
VALUES ('Film A'), ('Film B'), ('Film C');

-- 5. Create customer_review table
DROP TABLE IF EXISTS customer_review;
CREATE TABLE customer_review (
    review_id SERIAL PRIMARY KEY,
    film_id INTEGER REFERENCES new_film(id) ON DELETE CASCADE,
    language_id INTEGER REFERENCES language(language_id),
    title VARCHAR(255),
    score INTEGER CHECK(score BETWEEN 1 AND 10),
    review_text TEXT,
    last_update TIMESTAMP DEFAULT NOW()
);

-- 6. Add 2 reviews
INSERT INTO customer_review (film_id, language_id, title, score, review_text)
VALUES 
(1, 1, 'Amazing Film', 9, 'Loved the story and visuals.'),
(2, 2, 'Not Bad', 7, 'Entertaining but could be better.');

-- 7. Delete a film that has a review
DELETE FROM new_film WHERE id = 1;

-- EXERCISE 2 -----------------------------------------------

-- 1. Update language of some films
UPDATE film SET language_id = 2 WHERE film_id IN (1, 2, 3);

-- 2. Show foreign keys in customer table
SELECT 
    tc.constraint_name, 
    kcu.column_name, 
    ccu.table_name AS foreign_table_name, 
    ccu.column_name AS foreign_column_name 
FROM 
    information_schema.table_constraints AS tc 
    JOIN information_schema.key_column_usage AS kcu
      ON tc.constraint_name = kcu.constraint_name
    JOIN information_schema.constraint_column_usage AS ccu
      ON ccu.constraint_name = tc.constraint_name
WHERE constraint_type = 'FOREIGN KEY' AND tc.table_name = 'customer';

-- 3. Drop customer_review table (if exists)
DROP TABLE IF EXISTS customer_review;

-- 4. Count rentals not returned
SELECT COUNT(*) AS unreturned_rentals
FROM rental
WHERE return_date IS NULL;

-- 5. 30 most expensive unreturned movies
SELECT f.title, f.replacement_cost
FROM rental r
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
WHERE r.return_date IS NULL
ORDER BY f.replacement_cost DESC
LIMIT 30;

-- 6. Help your friend find 4 movies

-- 1st: About sumo, with Penelope Monroe
SELECT f.title
FROM film f
JOIN film_actor fa ON f.film_id = fa.film_id
JOIN actor a ON fa.actor_id = a.actor_id
WHERE a.first_name = 'Penelope' AND a.last_name = 'Monroe'
  AND f.description ILIKE '%sumo%';

-- 2nd: Short documentary (under 60 min), rated R
SELECT title
FROM film
WHERE length < 60 AND rating = 'R';

-- 3rd: Rented by Matthew Mahan, paid over $4, returned between 28 Jul–1 Aug 2005
SELECT f.title
FROM customer c
JOIN rental r ON c.customer_id = r.customer_id
JOIN payment p ON r.rental_id = p.rental_id
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
WHERE c.first_name = 'Matthew' AND c.last_name = 'Mahan'
  AND p.amount > 4
  AND r.return_date BETWEEN '2005-07-28' AND '2005-08-01';

-- 4th: Also watched by Matthew, contains "boat", expensive to replace
SELECT f.title
FROM customer c
JOIN rental r ON c.customer_id = r.customer_id
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
WHERE c.first_name = 'Matthew' AND c.last_name = 'Mahan'
  AND (f.title ILIKE '%boat%' OR f.description ILIKE '%boat%')
ORDER BY f.replacement_cost DESC
LIMIT 1;