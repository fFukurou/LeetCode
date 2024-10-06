-- https://leetcode.com/problems/project-employees-i/?envType=study-plan-v2&envId=top-sql-50
USE LEETCODE_DB;
DROP TABLE IF EXISTS project;
DROP TABLE IF EXISTS EMPLOYEE;
Create table If Not Exists Project (project_id int, employee_id int);
Create table If Not Exists Employee (employee_id int, name varchar(10), experience_years int);
Truncate table Project;
insert into Project (project_id, employee_id) values ('1', '1');
insert into Project (project_id, employee_id) values ('1', '2');
insert into Project (project_id, employee_id) values ('1', '3');
insert into Project (project_id, employee_id) values ('2', '1');
insert into Project (project_id, employee_id) values ('2', '4');
Truncate table Employee;
insert into Employee (employee_id, name, experience_years) values ('1', 'Khaled', '3');
insert into Employee (employee_id, name, experience_years) values ('2', 'Ali', '2');
insert into Employee (employee_id, name, experience_years) values ('3', 'John', '1');
insert into Employee (employee_id, name, experience_years) values ('4', 'Doe', '2');


SELECT * FROM PROJECT;
SELECT * FROM EMPLOYEE;

-- Write an SQL query that reports the average experience years of all the employees for each project, rounded to 2 digits.

SELECT project_id, ROUND(AVG(experience_years), 2) AS average_years FROM EMPLOYEE e
JOIN PROJECT p ON e.employee_id = p.employee_id
GROUP BY project_id;