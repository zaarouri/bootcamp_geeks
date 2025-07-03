---exerciseXp 1 :
SELECT CURRENT_DATABASE()


SELECT * from items 
ORDER BY price ASC



SELECT * from items 
WHERE price >= 80
Order by price DESC


SELECT * from customers
order by first_name ASC
limit 3


SELECT last_name from customers 
order by last_name DESC
---  Exercise 2 : dvdrental database
Select * from customer;


SELECT CONCAT(first_name , ' ', last_name ) as full_name  from customer;


Select DISTINCT create_date from customer;


SELECT * FROM CUSTOMER 
order by first_name DESC


-- Write a query to get the film ID, title, description, year of release and rental rate in ascending order according to their rental rate.

Select film_id , title, description, release_year, rental_rate from film
order by rental_rate ASC

-- Write a query to get the address, and the phone number of all customers living in the Texas district, these details can be found in the “address” table.

Select address, phone from address
where district = 'Texas'

-- Write a query to retrieve all movie details where the movie id is either 15 or 150.
select * from film
where film_id = 15 or film_id = 150


-- Write a query which should check if your favorite movie exists in the database. Have your query get the film ID, title, description, length and the rental rate, these details can be found in the “film” table.
select film_id, title, description, length, rental_rate from film
where title = 'Source Code'

-- No luck finding your movie? Maybe you made a mistake spelling the name. Write a query to get the film ID, title, description, length and the rental rate of all the movies starting with the two first letters of your favorite movie.
select film_id, title, description, length, rental_rate from film
where title like 'So%'


-- Write a query which will find the 10 cheapest movies.
select * from film
order by rental_rate ASC
limit 10


-- Not satisfied with the results. Write a query which will find the next 10 cheapest movies.
--Bonus: Try to not use LIMIT.

SELECT film_id, title, rental_rate
FROM film
ORDER BY rental_rate ASC, film_id ASC
OFFSET 10 ROWS FETCH NEXT 10 ROWS ONLY;
--Write a query which will join the data in the customer table and the payment table. You want to get the first name and last name from the curstomer table, as well as the amount and the date of every payment made by a customer, ordered by their id (from 1 to…).
select first_name, last_name, amount, payment_date from customer
join payment on customer.customer_id = payment.customer_id
order by customer.customer_id


--You need to check your inventory. Write a query to get all the movies which are not in inventory.
select * from film
where film_id not in (select film_id from inventory)

-- Write a query to find which city is in which country.
select city, country from city
join country on city.country_id = country.country_id


-- Bonus You want to be able to see how your sellers have been doing? Write a query to get the customer’s id, names (first and last), the amount and the date of payment ordered by the id of the staff member who sold them the dvd.
SELECT customer.customer_id, customer.customer_id, customer.first_name, customer.last_name,     payment.amount, payment.payment_date
FROM customer
JOIN payment ON customer.customer_id = payment.customer_id 
ORDER BY payment.staff_id ASC;
