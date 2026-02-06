-- Enable readable output format
.mode columns
.headers on

-- write your sql code here

SELECT orders.order_id
FROM orders JOIN customers
ON customers.customer_id = orders.customer_id
where customers.email = 'xjones@example.com'
