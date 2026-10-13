# Write your MySQL query statement below
select unique_id,name
from employees as A
left join
employeeUnI as B
on A.id=B.id;