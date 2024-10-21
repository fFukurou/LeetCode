-- https://leetcode.com/problems/customers-who-bought-all-products/?envType=study-plan-v2&envId=top-sql-50

use leetcode_db;
drop table if exists customer;
drop table if exists product;
Create table If Not Exists Customer (customer_id int, product_key int);
Create table Product (product_key int);
Truncate table Customer;
insert into Customer (customer_id, product_key) values ('1', '5');
insert into Customer (customer_id, product_key) values ('2', '6');
insert into Customer (customer_id, product_key) values ('3', '5');
insert into Customer (customer_id, product_key) values ('3', '6');
insert into Customer (customer_id, product_key) values ('1', '6');
Truncate table Product;
insert into Product (product_key) values ('5');
insert into Product (product_key) values ('6');

select * from customer;
select * from product;

-- Write a solution to report the customer ids from the Customer table that bought all the products in the Product table.
select distinct product_key from product;

select c1.customer_id, count(distinct c1.product_key) from customer c1
group by c1.customer_id
having count(c1.customer_id) = (select count(distinct p1.product_key) from product p1) and 
c1.product_key in (select count(distinct p2.product_key) from product p2);


# Write your MySQL query statement below

SELECT  customer_id FROM Customer GROUP BY customer_id
HAVING COUNT(distinct product_key) = (SELECT COUNT(product_key) FROM Product);




