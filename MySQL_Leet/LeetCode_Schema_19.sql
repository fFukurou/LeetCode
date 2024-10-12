-- https://leetcode.com/problems/find-followers-count/description/?envType=study-plan-v2&envId=top-sql-50


use leetcode_db;
drop table if exists followers;
Create table If Not Exists Followers(user_id int, follower_id int);
Truncate table Followers;
insert into Followers (user_id, follower_id) values ('0', '1');
insert into Followers (user_id, follower_id) values ('1', '0');
insert into Followers (user_id, follower_id) values ('2', '0');
insert into Followers (user_id, follower_id) values ('2', '1');

desc followers;
select * from followers;

-- Write a solution that will, for each user, return the number of followers.

select user_id, count(*) as followers_count
from followers
group by user_id
order by user_id asc;