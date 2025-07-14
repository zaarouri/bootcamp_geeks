-- part 1

/* 1.  Base table */
CREATE TABLE customer (
    id          SERIAL PRIMARY KEY,
    first_name  VARCHAR(100) NOT NULL,
    last_name   VARCHAR(100) NOT NULL
);

/* 2.  Profile table  
      – UNIQUE constraint on customer_id enforces “one profile per customer”. */
CREATE TABLE customer_profile (
    id           SERIAL PRIMARY KEY,
    customer_id  INTEGER UNIQUE REFERENCES customer(id) ON DELETE CASCADE,
    is_logged_in BOOLEAN DEFAULT FALSE
);

/* 3.  Insert customers */
INSERT INTO customer (first_name, last_name) VALUES
('John',   'Doe'),
('Jerome', 'Lalu'),
('Lea',    'Rive');

/* 4.  Insert profiles – subqueries guarantee we pick the correct id */
INSERT INTO customer_profile (is_logged_in, customer_id) VALUES
(TRUE,  (SELECT id FROM customer WHERE first_name='John'   AND last_name='Doe')),
(FALSE, (SELECT id FROM customer WHERE first_name='Jerome' AND last_name='Lalu'));

/* 5A. Logged-in customers’ first names (INNER JOIN) */
SELECT c.first_name
FROM   customer c
JOIN   customer_profile p ON p.customer_id = c.id
WHERE  p.is_logged_in;

/* 5B. Every customer + login flag, even if no profile (LEFT JOIN) */
SELECT
    c.first_name,
    COALESCE(p.is_logged_in, FALSE) AS is_logged_in          -- NULL ⇒ treat as FALSE
FROM customer c
LEFT JOIN customer_profile p ON p.customer_id = c.id;

/* 5C. How many customers are NOT logged in?
       Treat “no profile” as “not logged in”. */
SELECT COUNT(*) AS not_logged_in
FROM   customer c
LEFT   JOIN customer_profile p ON p.customer_id = c.id
WHERE  COALESCE(p.is_logged_in, FALSE) = FALSE;

-- part 2

/* 1.  Book table */
CREATE TABLE book (
    book_id SERIAL PRIMARY KEY,
    title   VARCHAR(200) NOT NULL,
    author  VARCHAR(200) NOT NULL
);

INSERT INTO book (title, author) VALUES
('Alice In Wonderland',  'Lewis Carroll'),
('Harry Potter',         'J.K Rowling'),
('To kill a mockingbird','Harper Lee');

/* 2.  Student table with age constraint (CHECK) */
CREATE TABLE student (
    student_id SERIAL PRIMARY KEY,
    name       VARCHAR(100) NOT NULL UNIQUE,
    age        INTEGER CHECK (age <= 15)
);

INSERT INTO student (name, age) VALUES
('John',    12),
('Lera',    11),
('Patrick', 10),
('Bob',     14);

/* 3.  Junction (Library) table  
      – Composite PK on both FKs forbids “same child borrows same book twice”.
      – ON DELETE/UPDATE CASCADE propagates changes. */
CREATE TABLE library (
    book_fk_id    INTEGER REFERENCES book(book_id)    ON DELETE CASCADE ON UPDATE CASCADE,
    student_fk_id INTEGER REFERENCES student(student_id) ON DELETE CASCADE ON UPDATE CASCADE,
    borrowed_date DATE,
    PRIMARY KEY (book_fk_id, student_fk_id)
);

/* 4.  Borrowing records (subqueries again) */
INSERT INTO library (book_fk_id, student_fk_id, borrowed_date) VALUES
((SELECT book_id    FROM book    WHERE title='Alice In Wonderland'),
 (SELECT student_id FROM student WHERE name='John'),
 '2022-02-15'),

((SELECT book_id    FROM book    WHERE title='To kill a mockingbird'),
 (SELECT student_id FROM student WHERE name='Bob'),
 '2021-03-03'),

((SELECT book_id    FROM book    WHERE title='Alice In Wonderland'),
 (SELECT student_id FROM student WHERE name='Lera'),
 '2021-05-23'),

((SELECT book_id    FROM book    WHERE title='Harry Potter'),
 (SELECT student_id FROM student WHERE name='Bob'),
 '2021-08-12');

/* 5A. Inspect the raw junction data */
SELECT * FROM library;

/* 5B. Friendly list: child name + book title (+ date if you like) */
SELECT
    s.name,
    b.title,
    l.borrowed_date
FROM library  l
JOIN student  s ON s.student_id = l.student_fk_id
JOIN book     b ON b.book_id    = l.book_fk_id
ORDER BY s.name, l.borrowed_date;

/* 5C. Average age of children who borrowed “Alice In Wonderland” */
SELECT ROUND(AVG(s.age),2) AS avg_age_alice
FROM   library l
JOIN   student s ON s.student_id = l.student_fk_id
JOIN   book    b ON b.book_id    = l.book_fk_id
WHERE  b.title = 'Alice In Wonderland';

/* 5D. Demonstrate cascade: delete Bob … */
DELETE FROM student WHERE name='Bob';

/* … and confirm his rows vanished from library */
SELECT * FROM library;

/* You should now see only John’s and Lera’s loans remaining. */
