-- Exercise 1 : DVD Rentals
--Get a list of all rentals which are out (have not been returned). How do we identify these films in the database?
select * from rental
where return_date is null
--Get a list of all customers who have not returned their rentals. Make sure to group your results.
select customer_id from rental
where return_date is null
group by customer_id
--Get a list of all the Action films with Joe Swank
-- i found a view in the database so i used it
select * from actor_info
where first_name = 'Joe' and last_name = 'Swank'
and film_info like 'Action%'

-- Exercise 2 – Happy Halloween
-- 1. Number of stores and their locations (city & country)
SELECT s.store_id, c.city, co.country
FROM store s
join address a on s.address_id = a.address_id
join city c on c.city_id = a.city_id
join country co on co.country_id = c.country_id
-- 2. Total viewing time per store (only returned items)
SELECT i.store_id,
       SUM(f.length) AS total_minutes,
       ROUND(SUM(f.length) / 60.0, 2) AS total_hours,
       ROUND(SUM(f.length) / 60.0 / 24.0, 2) AS total_days
FROM   inventory i
JOIN   film f ON i.film_id = f.film_id
JOIN   rental r ON i.inventory_id = r.inventory_id
WHERE  r.return_date IS NOT NULL
GROUP  BY i.store_id;

-- 3. All customers in cities where stores are located
SELECT DISTINCT c.customer_id,
       c.first_name,
       c.last_name,
       ci.city
FROM   customer c
JOIN   address a ON c.address_id = a.address_id
JOIN   city ci ON a.city_id = ci.city_id
WHERE  ci.city_id IN (
    SELECT a.city_id
    FROM store s
    JOIN address a ON s.address_id = a.address_id
);

-- 4. All customers in countries where stores are located
SELECT DISTINCT c.customer_id,
       c.first_name,
       c.last_name,
       co.country
FROM   customer c
JOIN   address a ON c.address_id = a.address_id
JOIN   city ci ON a.city_id = ci.city_id
JOIN   country co ON ci.country_id = co.country_id
WHERE  co.country_id IN (
    SELECT co.country_id
    FROM   store s
    JOIN   address a ON s.address_id = a.address_id
    JOIN   city ci ON a.city_id = ci.city_id
    JOIN   country co ON ci.country_id = co.country_id
);

-- 5. "Safe" movies list (no Horror, no scary words)
SELECT COUNT(*) AS safe_movies,
       SUM(f.length) AS total_minutes,
       ROUND(SUM(f.length) / 60.0, 2) AS total_hours,
       ROUND(SUM(f.length) / 60.0 / 24.0, 2) AS total_days
FROM   film f
WHERE  f.film_id NOT IN (
           SELECT fc.film_id
           FROM   film_category fc
           JOIN   category c ON fc.category_id = c.category_id
           WHERE  c.name = 'Horror'
       )
  AND   LOWER(f.title) NOT SIMILAR TO '%(beast|monster|ghost|dead|zombie|undead)%'
  AND   LOWER(f.description) NOT SIMILAR TO '%(beast|monster|ghost|dead|zombie|undead)%';

-- 6. "General" total viewing time (all returned films in inventory)
SELECT SUM(f.length) AS total_minutes,
       ROUND(SUM(f.length) / 60.0, 2) AS total_hours,
       ROUND(SUM(f.length) / 60.0 / 24.0, 2) AS total_days
FROM   inventory i
JOIN   film f ON i.film_id = f.film_id
JOIN   rental r ON i.inventory_id = r.inventory_id
WHERE  r.return_date IS NOT NULL;