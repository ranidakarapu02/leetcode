# Write your MySQL query statement below
select round(sum(tiv_2016),2)tiv_2016 from insurance n where not exists
(select 1 from insurance i where n.pid!=i.pid and n.lat=i.lat and n.lon=i.lon
)and exists(select 1 from insurance i where n.pid!=i.pid and n.tiv_2015=i.tiv_2015);