
-- part 1: Create tables

-- 1: Users table
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE
);

-- 2: Product orders table
CREATE TABLE product_orders (
    order_id SERIAL PRIMARY KEY,
    order_date DATE DEFAULT CURRENT_DATE,
    user_id INT REFERENCES users(user_id) ON DELETE CASCADE
);

-- 3: Items table
CREATE TABLE items (
    item_id SERIAL PRIMARY KEY,
    order_id INT REFERENCES product_orders(order_id) ON DELETE CASCADE,
    product_name VARCHAR(100) NOT NULL,
    quantity INT DEFAULT 1,
    price NUMERIC(10, 2) NOT NULL
);

-- part 2: Insert data

-- 1: Insert users
INSERT INTO users (username) VALUES 
    ('abdelmounime'),
    ('sarah');

-- 2: Insert orders
INSERT INTO product_orders (user_id) VALUES 
    ((SELECT user_id FROM users WHERE username = 'abdelmounime')),
    ((SELECT user_id FROM users WHERE username = 'abdelmounime')),
    ((SELECT user_id FROM users WHERE username = 'sarah'));

-- 3: Insert items
INSERT INTO items (order_id, product_name, quantity, price) VALUES
    (1, 'Mouse',     2, 25.50),
    (1, 'Keyboard',  1, 45.00),
    (2, 'Monitor',   1, 150.00),
    (3, 'USB Cable', 3, 5.00);

-- part 3: Queries

-- 1: Total price for each order
SELECT 
    order_id,
    SUM(quantity * price) AS total_price
FROM items
GROUP BY order_id;

-- 2: Total price for order with id = 1
SELECT 
    order_id,
    SUM(quantity * price) AS total_price
FROM items
WHERE order_id = 1
GROUP BY order_id;

-- 3: Total price for order id = 2 made by user id = 1
SELECT 
    po.user_id,
    po.order_id,
    SUM(i.quantity * i.price) AS total_price
FROM items i
JOIN product_orders po ON i.order_id = po.order_id
WHERE po.user_id = 1 AND po.order_id = 2
GROUP BY po.user_id, po.order_id;

-- 4: All orders with username and total price
SELECT 
    u.username,
    po.order_id,
    SUM(i.quantity * i.price) AS total_price
FROM users u
JOIN product_orders po ON u.user_id = po.user_id
JOIN items i ON po.order_id = i.order_id
GROUP BY u.username, po.order_id
ORDER BY u.username;
