SELECT current_database();


CREATE TABLE IF NOT EXISTS students(
    id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    BIRTH_DATE DATE 
);
INSERT INTO students (first_name, last_name, birth_date)
VALUES 
  ('Marc', 'Dupont','1998-11-02'),
  ('Yoan', 'Durant', '2010-03-12'),
  ('Lea', 'Martin', '1987-07-24'),
  ('Sarah', 'Benichou', '1996-04-07'),
  ('Lea', 'Dupont', '2003-06-14'),
  ('Omer', 'Simpson', '1980-03-10');


  SELECT first_name, last_name FROM students WHERE id = 2;

  SELECT first_name, last_name FROM students WHERE last_name = 'benichou' AND first_name = 'Marc' ;

  SELECT first_name, last_name FROM students WHERE last_name = 'benichou' OR first_name = 'Marc' ;


SELECT first_name, last_name FROM students
WHERE first_name ILIKE '%a%';
    
SELECT first_name, last_name FROM students
WHERE first_name ILIKE 'a%';

SELECT first_name, last_name FROM students
WHERE first_name ILIKE '%a';


SELECT first_name, last_name FROM students
WHERE first_name ~ '.a.$';


SELECT first_name, last_name FROM students
WHERE id IN (1, 3);



--   continue here for the next exercise

SELECT first_name, last_name, birth_date
FROM students
ORDER BY last_name ASC
LIMIT 4;

SELECT first_name, last_name, birth_date
FROM students
ORDER BY birth_date DESC
LIMIT 1;

SELECT first_name, last_name, birth_date
FROM students
OFFSET 2
LIMIT 3;

