-- 1. Last two customers alphabetically (exclude id)
SELECT first_name, last_name
FROM   customers
ORDER  BY last_name DESC, first_name DESC
LIMIT  2;

-- 2. Delete purchases made by Scott
DELETE FROM purchases
WHERE  customer_id = (
        SELECT id
        FROM   customers
        WHERE  first_name = 'Scott'
          AND  last_name  = 'Scott'
      );

-- 3. Check if Scott still exists in customers table
SELECT *
FROM   customers
WHERE  first_name = 'Scott'
  AND  last_name  = 'Scott';

-- 4. Purchases with customer info using LEFT JOIN
SELECT p.id,
       p.item_id,
       p.quantity_purchased,
       COALESCE(c.first_name, '') AS first_name,
       COALESCE(c.last_name,  '') AS last_name
FROM   purchases p
LEFT  JOIN customers c ON c.id = p.customer_id;

-- 5. Purchases with customer info using INNER JOIN
SELECT p.id,
       p.item_id,
       p.quantity_purchased,
       c.first_name,
       c.last_name
FROM   purchases p
INNER JOIN customers c ON c.id = p.customer_id;