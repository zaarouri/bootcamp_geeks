
-- Create tables
CREATE TABLE customers();  
CREATE TABLE items();      

ALTER TABLE items ADD COLUMN id SERIAL PRIMARY KEY;
ALTER TABLE items ADD COLUMN name VARCHAR(50);
ALTER TABLE items ADD COLUMN price DECIMAL(10,2);

ALTER TABLE customers ADD COLUMN id SERIAL PRIMARY KEY;
ALTER TABLE customers ADD COLUMN first_name VARCHAR(50);
ALTER TABLE customers ADD COLUMN last_name VARCHAR(50);

INSERT INTO items (name, price) VALUES ('small desk', 100);
INSERT INTO items (name, price) VALUES ('large desk', 300);
INSERT INTO items (name, price) VALUES ('fan', 80);

INSERT INTO customers (first_name, last_name) VALUES ('Greg', 'Jones');
INSERT INTO customers (first_name, last_name) VALUES ('Sandra', 'Jones');
INSERT INTO customers (first_name, last_name) VALUES ('Scott', 'Scott');
INSERT INTO customers (first_name, last_name) VALUES ('Trevor', 'Green');
INSERT INTO customers (first_name, last_name) VALUES ('Melanie', 'Johnson');

SELECT * FROM items;
SELECT * FROM customers;



SELECT * FROM items
WHERE price >80;



SELECT * FROM items
WHERE price <300;

SELECT * FROM customers
WHERE last_name = 'Smith';

SELECT * FROM customers
WHERE last_name = 'Jones';


SELECT * FROM customers
WHERE last_name NOT LIKE 'Scott';


CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer_id INT,
    item_id INT,
    FOREIGN KEY (customer_id) REFERENCES customers(id),
    FOREIGN KEY (item_id) REFERENCES items(id)
);

INSERT INTO orders (customer_id, item_id) VALUES (1, 2);
INSERT INTO orders (customer_id, item_id) VALUES (3, 1);
INSERT INTO orders (customer_id, item_id) VALUES (4, 1);
INSERT INTO orders (customer_id, item_id) VALUES (1, 3);
INSERT INTO orders (customer_id, item_id) VALUES (2, 2);