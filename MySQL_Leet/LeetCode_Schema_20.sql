-- https://leetcode.com/problems/biggest-single-number/description/?envType=study-plan-v2&envId=top-sql-50

use leetcode_db;
drop table if exists mynumbers;
Create table If Not Exists MyNumbers (num int);
Truncate table MyNumbers;
insert into MyNumbers (num) values ('8');
insert into MyNumbers (num) values ('8');
insert into MyNumbers (num) values ('3');
insert into MyNumbers (num) values ('3');
insert into MyNumbers (num) values ('1');
insert into MyNumbers (num) values ('4');
insert into MyNumbers (num) values ('5');
insert into MyNumbers (num) values ('6');

desc MyNumbers;
select * from MyNumbers;

-- A single number is a number that appeared only once in the MyNumbers table.

--  Find the largest single number. If there is no single number, report null.

select ifnull(max(num), null) as num from mynumbers
where num in 
(select num from mynumbers m2
group by num
having count(*) = 1);
