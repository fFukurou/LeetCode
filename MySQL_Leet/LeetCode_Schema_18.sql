-- https://leetcode.com/problems/classes-more-than-5-students/description/?envType=study-plan-v2&envId=top-sql-50
USE LEETCODE_DB;

DROP TABLE IF EXISTS COURSES;
Create table If Not Exists Courses (student varchar(255), class varchar(255));
Truncate table Courses;
insert into Courses (student, class) values ('A', 'Math');
insert into Courses (student, class) values ('B', 'English');
insert into Courses (student, class) values ('C', 'Math');
insert into Courses (student, class) values ('D', 'Biology');
insert into Courses (student, class) values ('E', 'Math');
insert into Courses (student, class) values ('F', 'Computer');
insert into Courses (student, class) values ('G', 'Math');
insert into Courses (student, class) values ('H', 'Math');
insert into Courses (student, class) values ('I', 'Math');


-- Write a solution to find all the classes that have at least five students.

DESC COURSES;
SELECT * FROM COURSES;

select class, count(class)from courses group by class;

select c1.class from courses c1
join (select class, count(class)from courses group by class) 
courses on c1.class = courses.class
group by class
having count(*) >= 5;

select class from courses group by class having count(*) >= 5;