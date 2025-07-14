CREATE TABLE actors(
 actor_id SERIAL PRIMARY KEY,
 first_name VARCHAR (50) NOT NULL,
 last_name VARCHAR (100) NOT NULL,
 age DATE NOT NULL,
 number_oscars SMALLINT NOT NULL
)
INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES 
  ('Tom', 'Hanks', '1956-07-03', 5),
  ('Meryl', 'Streep', '1949-06-22', 3),
  ('Robert', 'De Niro', '1943-08-17', 6),
  ('Meryl', 'Streep', '1949-06-22', 3),
  ('Tom', 'Hanks', '1956-07-03', 5),
  ('Meryl', 'Streep', '1949-06-22', 3);

SELECT COUNT(actor_id) from actors


insert into actors (first_name, last_name, age, number_oscars)
VALUES 
  ('', '', '', 5);
-- not null error 