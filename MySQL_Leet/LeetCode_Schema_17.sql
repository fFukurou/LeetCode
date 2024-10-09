-- https://leetcode.com/problems/product-sales-analysis-iii/description/?envType=study-plan-v2&envId=top-sql-50

USE LEETCODE_DB;

DROP TABLE IF EXISTS SALES;
DROP TABLE IF EXISTS PRODUCT;
Create table If Not Exists Sales (sale_id int, product_id int, year int, quantity int, price int);
Create table If Not Exists Product (product_id int, product_name varchar(10));
Truncate table Sales;
insert into Sales (sale_id, product_id, year, quantity, price) values ('1', '100', '2008', '10', '5000');
insert into Sales (sale_id, product_id, year, quantity, price) values ('2', '100', '2009', '12', '5000');
insert into Sales (sale_id, product_id, year, quantity, price) values ('7', '200', '2011', '15', '9000');
Truncate table Product;
insert into Product (product_id, product_name) values ('100', 'Nokia');
insert into Product (product_id, product_name) values ('200', 'Apple');
insert into Product (product_id, product_name) values ('300', 'Samsung');

-- Write a solution to select the product id, year, quantity, and price for the first year of every product sold.

select s.product_id, s.year as first_year, s.quantity, s.price from sales s
join product p on p.product_id = s.product_id
where s.year in (select min(year) from sales s2 group by s2.product_id)
;

select s.product_id, s.year as first_year, s.quantity, s.price from sales s
join product p on p.product_id = s.product_id
where s.year = (select min(year) from sales s2 where s.product_id = s2.product_id)
;

select s.product_id, s.year as first_year, s.quantity, s.price from sales s
join product p on p.product_id = s.product_id
where s.year = (select min(s2.year) from sales s2 where s.product_id = s2.product_id)
;

SELECT product_id, MIN(year) AS first_year
    FROM sales
    GROUP BY product_id;



SELECT s.product_id, s.year AS first_year, s.quantity, s.price 
FROM sales s
JOIN ( -- joining the products table is not even necessary...
    SELECT product_id, MIN(year) AS first_year
    FROM sales
    GROUP BY product_id
) min_years ON s.product_id = min_years.product_id AND s.year = min_years.first_year;
