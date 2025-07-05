create TABLE customer(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) ,
    last_name VARCHAR(100) NOT NULL
);
CREATE TABLE profile (
    id SERIAL PRIMARY KEY,
    customer_id INT  UNIQUE REFERENCES customer(id),
    username VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL,
    is_logged_in BOOLEAN  default false
);

insert into customer (first_name, last_name) VALUES ('John', 'Doe');
insert into customer (first_name, last_name) VALUES ('Jerome', 'Lalu');
insert into customer (first_name, last_name) VALUES ('Lea', 'Rive');





DELETE FROM customer c
USING (
    SELECT id,
           ROW_NUMBER() OVER (PARTITION BY first_name, last_name ORDER BY id) AS rn
    FROM   customer
) dup
WHERE c.id = dup.id
  AND dup.rn > 1
  AND dup.first_name = 'John'
  AND dup.last_name  = 'Doe';

SELECT id
FROM   customer
WHERE  first_name = 'John' AND last_name = 'Doe';

-- John is logged in
INSERT INTO profile (is_Logged_In, customer_id)
VALUES (
    TRUE,(SELECT id FROM customer WHERE first_name = 'John' AND last_name = 'Doe')
);

-- Jerome is not logged in
INSERT INTO profile (is_Logged_In, customer_id)
VALUES (
    FALSE,
    (SELECT id FROM customer WHERE first_name = 'Jerome' AND last_name = 'Lalu')
);