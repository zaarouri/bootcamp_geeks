-- ============================================================
-- Exercise 1 : DVD Rental
-- ------------------------------------------------------------

-- 1. Films per rating (descending)
SELECT rating, COUNT(*) AS film_count
FROM film
GROUP BY rating
ORDER BY film_count DESC;

-- 2. Family-friendly films (G or PG-13, < 2 h, rental_rate < 3)
SELECT title, rating, length, rental_rate
FROM   film
WHERE  rating IN ('G', 'PG-13')
  AND  length     < 120
  AND  rental_rate < 3.00
ORDER BY title;

-- 3. Update the chosen customer's personal data
UPDATE customer
SET    first_name = 'Abdelmounime',
       last_name  = 'Zaarouri',
       email      = 'abdelmounime.zaarouri@gmail.com'
WHERE  customer_id = 50;      -- change ID if needed

-- 4. Update the same customer's address
UPDATE address a
SET    address      = '123 Main St',
       district     = 'Casablanca-Anfa',
       city_id      = 449,    -- must exist in city table
       phone        = '0600-123-456',
       last_update  = NOW()
FROM   customer c
WHERE  c.customer_id = 50
  AND  c.address_id  = a.address_id;

-- ============================================================
-- Exercise 2 : students table
-- ------------------------------------------------------------

-- 0. Ensure math_grade column exists
ALTER TABLE students
ADD COLUMN IF NOT EXISTS math_grade INTEGER;

-- 1. Update twins' birth dates
UPDATE students
SET    birth_date = '1998-11-02'
WHERE  (first_name, last_name) IN (('Lea','Benichou'),
                                   ('Marc','Benichou'));

-- 2. Correct David Grez => Guez
UPDATE students
SET    last_name = 'Guez'
WHERE  first_name = 'David' AND last_name = 'Grez';

-- 3. Delete Lea Benichou record
DELETE FROM students
WHERE  first_name = 'Lea' AND last_name = 'Benichou';

-- 4. Counts
SELECT COUNT(*) AS total_students FROM students;
SELECT COUNT(*) AS born_after_2000
FROM   students
WHERE  birth_date > '2000-01-01';

-- 5. Assign math grades
UPDATE students SET math_grade = 80 WHERE id = 1;
UPDATE students SET math_grade = 90 WHERE id IN (2,4);
UPDATE students SET math_grade = 40 WHERE id = 6;

-- 6. Students scoring above 83
SELECT COUNT(*) AS above_83
FROM   students
WHERE  math_grade > 83;

-- 7. Add duplicate row for Omer Simpson (retake grade 70)
INSERT INTO students (first_name, last_name, birth_date, math_grade)
SELECT first_name, last_name, birth_date, 70
FROM   students
WHERE  first_name = 'Omer' AND last_name = 'Simpson'
LIMIT  1;

-- 8. Number of grades per student
SELECT first_name,
       last_name,
       COUNT(math_grade) AS total_grade
FROM   students
GROUP  BY first_name, last_name
ORDER  BY last_name, first_name;

-- 9. Sum of all grades
SELECT SUM(math_grade) AS sum_of_grades
FROM   students;

-- ============================================================
-- Exercise 3 : items, customers, purchases
-- ------------------------------------------------------------

-- Part I : table + inserts
CREATE TABLE IF NOT EXISTS purchases (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER  NOT NULL REFERENCES customers(id),
    item_id     INTEGER  NOT NULL REFERENCES items(id),
    quantity_purchased INTEGER NOT NULL CHECK (quantity_purchased > 0)
);

INSERT INTO purchases (customer_id, item_id, quantity_purchased) VALUES
  ( (SELECT id FROM customers WHERE first_name='Scott'   AND last_name='Scott'),
    (SELECT id FROM items     WHERE name='fan'),
    1 ),
  ( (SELECT id FROM customers WHERE first_name='Melanie' AND last_name='Johnson'),
    (SELECT id FROM items     WHERE name='large desk'),
    10 ),
  ( (SELECT id FROM customers WHERE first_name='Greg'    AND last_name='Jones'),
    (SELECT id FROM items     WHERE name='small desk'),
    2 );

-- Part II : queries

-- A. All purchases
SELECT * FROM purchases;

-- B. Purchases with customer names
SELECT p.id, c.first_name, c.last_name,
       p.item_id, p.quantity_purchased
FROM   purchases p
JOIN   customers c ON c.id = p.customer_id;

-- C. Purchases of customer_id = 5
SELECT * FROM purchases WHERE customer_id = 5;

-- D. Customers who bought both a large and a small desk
SELECT DISTINCT c.id, c.first_name, c.last_name
FROM   customers  c
JOIN   purchases  p1 ON p1.customer_id = c.id
JOIN   items      i1 ON i1.id = p1.item_id AND i1.name = 'large desk'
JOIN   purchases  p2 ON p2.customer_id = c.id
JOIN   items      i2 ON i2.id = p2.item_id AND i2.name = 'small desk';

-- E. Customers with purchases and item names
SELECT DISTINCT c.first_name, c.last_name, i.name AS item_name
FROM   purchases p
JOIN   customers c ON c.id = p.customer_id
JOIN   items     i ON i.id = p.item_id
ORDER  BY c.last_name, c.first_name;

-- F. Attempt to insert a purchase without an item_id (expected to fail)
-- INSERT INTO purchases (customer_id, item_id, quantity_purchased)
-- VALUES (1, NULL, 3);
-- This fails because item_id is NOT NULL and has a foreign-key constraint.
