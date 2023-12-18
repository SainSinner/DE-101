--Total Sales
select
ROUND(sum(dw.sales_fact.sales),2) as Total_Sales
from
dw.sales_fact;

--Total Profit
select
ROUND(sum(dw.sales_fact.profit),2) as Total_Profit
from
dw.sales_fact;

--Profit Ratio
select
ROUND((sum(dw.sales_fact.profit)/sum(dw.sales_fact.sales))*100,2) as Profit_Ratio
from
dw.sales_fact;

--Profit per Order
SELECT t1.order_id AS res_0, sum(t1.profit) AS res_1, t1.profit AS res_2
FROM db2.dw.sales_fact AS t1
GROUP BY res_0, res_2
ORDER BY res_2 DESC NULLS LAST, res_0 ASC NULLS FIRST
LIMIT 100 OFFSET 0;

--Sales per Customer
SELECT t5.customer_name AS res_0, sum(t1.sales) AS res_1, t1.sales AS res_2
FROM db2.dw.sales_fact AS t1 JOIN db2.dw.customer_dim AS t5 ON t1.cust_id = t5.cust_id
GROUP BY res_0, res_2
ORDER BY res_2 DESC NULLS LAST, res_0 ASC NULLS FIRST
LIMIT 100 OFFSET 0;

--Avg. Discount
SELECT ROUND(avg(t1.discount) * 100, 2) AS res_0
FROM db2.dw.sales_fact AS t1
LIMIT 1000001;

--Monthly Sales by Segment (табличка и график)
SELECT t4.segment AS res_0, t6.month AS res_1, sum(t1.sales) AS res_2
FROM
db2.dw.sales_fact AS t1 JOIN db2.dw.product_dim AS t4 ON t1.prod_id = t4.prod_id
JOIN
db2.dw.calendar_dim AS t6
ON t1.order_date_id = t6.dateid
GROUP BY res_0, res_1
ORDER BY res_0 ASC NULLS FIRST, res_1 ASC NULLS FIRST
LIMIT 100001

SELECT t4.segment AS res_0, sum(t1.sales) AS res_1
FROM db2.dw.sales_fact AS t1 JOIN db2.dw.product_dim AS t4 ON t1.prod_id = t4.prod_id
GROUP BY res_0
LIMIT 100001

SELECT t6.month AS res_0, sum(t1.sales) AS res_1
FROM db2.dw.sales_fact AS t1 JOIN db2.dw.calendar_dim AS t6 ON t1.order_date_id = t6.dateid
GROUP BY res_0
LIMIT 100001

SELECT sum(t1.sales) AS res_0
FROM db2.dw.sales_fact AS t1
LIMIT 100001;

SELECT t6.month AS res_0, t4.segment AS res_1, sum(t1.sales) AS res_2
FROM
db2.dw.sales_fact AS t1 JOIN db2.dw.product_dim AS t4 ON t1.prod_id = t4.prod_id
JOIN
db2.dw.calendar_dim AS t6
ON t1.order_date_id = t6.dateid
GROUP BY res_0, res_1
LIMIT 1000001;

--Monthly Sales by Product Category (табличка и график)
SELECT
    orders.category,
    EXTRACT('MONTH' FROM orders.order_date) AS month,
    SUM(orders.sales) AS sales
FROM orders
GROUP BY month, orders.category
ORDER BY month, orders.category;

--Sales by Product Category over time (Продажи по категориям)
SELECT t4.category AS res_0, t6.month AS res_1, sum(t1.sales) AS res_2
FROM
db2.dw.sales_fact AS t1 JOIN db2.dw.product_dim AS t4 ON t1.prod_id = t4.prod_id
JOIN
db2.dw.calendar_dim AS t6
ON t1.order_date_id = t6.dateid
GROUP BY res_0, res_1
ORDER BY res_0 ASC NULLS FIRST, res_1 ASC NULLS FIRST
LIMIT 100001

SELECT t4.category AS res_0, sum(t1.sales) AS res_1
FROM db2.dw.sales_fact AS t1 JOIN db2.dw.product_dim AS t4 ON t1.prod_id = t4.prod_id
GROUP BY res_0
LIMIT 100001

SELECT t6.month AS res_0, sum(t1.sales) AS res_1
FROM db2.dw.sales_fact AS t1 JOIN db2.dw.calendar_dim AS t6 ON t1.order_date_id = t6.dateid
GROUP BY res_0
LIMIT 100001

SELECT sum(t1.sales) AS res_0
FROM db2.dw.sales_fact AS t1
LIMIT 100001;

SELECT t6.month AS res_0, t4.category AS res_1, sum(t1.sales) AS res_2
FROM
db2.dw.sales_fact AS t1 JOIN db2.dw.product_dim AS t4 ON t1.prod_id = t4.prod_id
JOIN
db2.dw.calendar_dim AS t6
ON t1.order_date_id = t6.dateid
GROUP BY res_0, res_1
LIMIT 1000001;

--Customer Ranking
SELECT t5.customer_name AS res_0, sum(t1.sales) AS res_1, sum(t1.profit) AS res_2, t1.sales AS res_3
FROM db2.dw.sales_fact AS t1 JOIN db2.dw.customer_dim AS t5 ON t1.cust_id = t5.cust_id
GROUP BY res_0, res_3
ORDER BY res_3 DESC NULLS LAST, res_0 ASC NULLS FIRST
LIMIT 100 OFFSET 0;

--Sales per state
SELECT t3.state AS res_0, sum(t1.sales) AS res_1
FROM db2.dw.sales_fact AS t1 JOIN db2.dw.geo_dim AS t3 ON t1.geo_id = t3.geo_id
GROUP BY res_0
LIMIT 1000001;
