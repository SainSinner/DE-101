select
city,
count( distinct order_id) as number_orders,
sum(sales) as revenue
from public.orders o
where category in ('Furniture', 'Technology')
group by 1
having sum(sales) > 10000
order by revenue desc;

select
count(*),
count(distinct o.order_id)
from orders o left join "returns" r on o.order_id = r.oreder_id;

--Total Sales
select
ROUND(sum(orders.sales),2) as Total_Sales
from
orders;

--Total Profit
select
ROUND(sum(orders.profit),2) as Total_Profit
from
orders;

--Profit Ratio
select
ROUND((sum(orders.profit)/sum(orders.sales))*100,2) as Profit_Ratio
from
orders;

--Profit per Order
select orders.order_id, SUM(orders.profit) as Profit_per_Order
from
orders
group by orders.order_id;

--Sales per Customer
select orders.customer_id , SUM(orders.sales) as Sales_per_Customer
from
orders
group by orders.customer_id;

--Avg. Discount
select round((AVG(orders.discount)*100),2) as Avg_Discount
from
orders;

--Monthly Sales by Segment (табличка и график)
SELECT
    orders.segment,
    EXTRACT('MONTH' FROM orders.order_date) AS month,
    SUM(orders.sales) AS sales
FROM orders
GROUP BY EXTRACT('MONTH' FROM orders.order_date), orders.segment
ORDER BY month, orders.segment;

--Monthly Sales by Product Category (табличка и график)
SELECT
    orders.category,
    EXTRACT('MONTH' FROM orders.order_date) AS month,
    SUM(orders.sales) AS sales
FROM orders
GROUP BY month, orders.category
ORDER BY month, orders.category;

--Sales by Product Category over time (Продажи по категориям)
SELECT
    orders.category,
    SUM(orders.sales) AS sales
FROM orders
GROUP BY orders.category
ORDER BY orders.category;

--Sales and Profit by Customer
SELECT
    orders.customer_id,
    orders.customer_name,
    ROUND(SUM(orders.sales),2) AS sales,
    ROUND(SUM(orders.profit),2) AS profit
FROM orders
GROUP BY orders.customer_id, orders.customer_name
ORDER BY profit DESC;

--Customer Ranking
SELECT
    orders.customer_id,
    orders.customer_name,
    ROUND(SUM(orders.sales),2) AS sales,
    ROUND(SUM(orders.profit),2) AS profit
FROM orders
GROUP BY orders.customer_id, orders.customer_name
ORDER BY sales DESC;

--Sales per region
SELECT
    orders.region,
    people.person,
    ROUND(SUM(orders.sales),2) AS sales
FROM orders
INNER JOIN people ON orders.region = people.region
GROUP BY orders.region, people.person
ORDER BY sales DESC;
