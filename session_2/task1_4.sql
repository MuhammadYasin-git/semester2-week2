-- Enable readable output format
.mode columns
.headers on

-- write your sql code here

SELECT DISTINCT name
FROM products
WHERE price < 2
