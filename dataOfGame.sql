create database gameScore;
use gamescore;
create table  temp1 select * from gamesale inner join tbexport on (gamesale.GameName=tbexport.GameName);
alter table tbexport change column name gamename varchar(255);

select * from gamesale group by Publisher order by sum(Global_sales) desc;

select Publisher,sum(Global_sales) from gamesale group by Publisher order by sum(Global_sales) desc;

select sum(Global_sales),sum(NA_Sales),sum(EU_Sales),sum(JP_Sales),sum(Other_Sales) from gamesale;

select sum(Global_sales) from gamesale where publishyear="2016" group by publisher,publishyear order by sum(Global_sales) desc;

select sum(Total_shipped),publisher from gamesale_critical where publishyear like "%2019%" group by publisher,publishyear order by sum(Total_shipped) desc;

