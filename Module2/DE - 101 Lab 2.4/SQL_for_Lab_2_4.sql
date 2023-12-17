USE orders;
-- ************************************** calendar
DROP table if exists calendar;

CREATE TABLE calendar
(
 "date"     date NOT NULL,
 year     INTEGER NOT NULL,
 quarter  INTEGER NOT NULL,
 month    INTEGER NOT NULL,
 week     INTEGER NOT NULL,
 week_day INTEGER NOT NULL,
 CONSTRAINT PK_1 PRIMARY KEY ( "date" )
);

-- наполнение таблицы calendar
INSERT INTO calendar (date, year, quarter, month, week, week_day)
SELECT DISTINCT orders.order_date AS date,
                CAST(extract(YEAR FROM orders.order_date) AS INTEGER) AS year,
                CAST(extract(QUARTER FROM orders.order_date) AS INTEGER) AS quarter,
                CAST(extract(MONTH FROM orders.order_date) AS INTEGER) AS month,
                CAST(extract(WEEK FROM orders.order_date) AS INTEGER) AS week,
                CAST(extract(ISODOW FROM orders.order_date) AS INTEGER) AS week_day
FROM orders
UNION
SELECT DISTINCT orders.ship_date AS date,
                CAST(extract(YEAR FROM orders.ship_date) AS INTEGER) AS year,
                CAST(extract(QUARTER FROM orders.ship_date) AS INTEGER) AS quarter,
                CAST(extract(MONTH FROM orders.ship_date) AS INTEGER) AS month,
                CAST(extract(WEEK FROM orders.ship_date) AS INTEGER) AS week,
                CAST(extract(ISODOW FROM orders.ship_date) AS INTEGER) AS week_day
FROM orders;


-- ************************************** geography
DROP table if exists geography;

CREATE TABLE geography
(
 geo_id      serial NOT NULL,
 country     varchar(13) NOT NULL,
 city        varchar(17) NOT NULL,
 "state"       varchar(20) NOT NULL,
 region      varchar(7) NOT NULL,
 postal_code varchar(10) NOT NULL,
 CONSTRAINT PK_2 PRIMARY KEY ( geo_id )
);

-- фиксим проблему Null postal_code для города Burlington
UPDATE orders
set postal_code = '05401'
WHERE city = 'Burlington' AND postal_code IS NULL;

-- наполнение таблицы geography
INSERT INTO geography (country, city, state, region, postal_code)
SELECT DISTINCT
    orders.country,
    orders.city,
    orders.state,
    orders.region,
    orders.postal_code
FROM orders;

-- ************************************** product
DROP table if exists product;

CREATE TABLE product
(
 product_id   serial NOT NULL,
 category     varchar(15) NOT NULL,
 subcategory  varchar(11) NOT NULL,
 segment      varchar(11) NOT NULL,
 product_name varchar(127) NOT NULL,
 CONSTRAINT PK_3 PRIMARY KEY ( product_id )
);

-- наполнение таблицы product
INSERT INTO product (category, subcategory, segment, product_name)
SELECT DISTINCT
    orders.category,
    orders.subcategory,
    orders.segment,
    orders.product_name
FROM orders;

-- ************************************** shipping
DROP table if exists shipping;

CREATE TABLE shipping
(
 ship_id   serial NOT NULL,
 ship_mode varchar(14) NOT NULL,
 CONSTRAINT PK_4 PRIMARY KEY ( ship_id )
);

-- наполнение таблицы shipping
INSERT INTO shipping (ship_mode)
SELECT DISTINCT
    orders.ship_mode
FROM orders;

-- ************************************** sales_fact

DROP table if exists sales_fact;

CREATE TABLE sales_fact
(
 row_id     INTEGER NOT NULL,
 order_id   varchar(14) NOT NULL,
 sales      numeric(9,4) NOT NULL,
 quantity   INTEGER NOT NULL,
 discount   numeric(4,2) NOT NULL,
 profit     numeric(21,16) NOT NULL,
 ship_id    int NOT NULL,
 product_id int NOT NULL,
 geo_id     int NOT NULL,
 order_date date NOT NULL,
 ship_date  date NOT NULL,
 CONSTRAINT PK_5 PRIMARY KEY ( row_id ),
 CONSTRAINT FK_2 FOREIGN KEY ( ship_id ) REFERENCES shipping ( ship_id ),
 CONSTRAINT FK_3 FOREIGN KEY ( product_id ) REFERENCES product ( product_id ),
 CONSTRAINT FK_4 FOREIGN KEY ( geo_id ) REFERENCES geography ( geo_id )
);

CREATE INDEX FK_2 ON sales_fact
(
 ship_id
);

CREATE INDEX FK_3 ON sales_fact
(
 product_id
);

CREATE INDEX FK_4 ON sales_fact
(
 geo_id
);

-- наполнение таблицы shipping
INSERT INTO sales_fact (row_id,
                        order_id,
                        sales,
                        quantity,
                        discount,
                        profit,
                        ship_id,
                        product_id,
                        geo_id,
                        order_date,
                        ship_date)
SELECT
    orders.row_id,
    orders.order_id,
    orders.sales,
    orders.quantity,
    orders.discount,
    orders.profit,
    shipping.ship_id,
    product.product_id,
    geography.geo_id,
    orders.order_date,
    orders.ship_date
FROM orders
INNER JOIN shipping ON orders.ship_mode = shipping.ship_mode
INNER JOIN product ON orders.product_name = product.product_name AND orders.category = product.category AND orders.subcategory = product.subcategory AND orders.segment = product.segment
INNER JOIN geography ON orders.postal_code = geography.postal_code AND orders.city = geography.city AND orders.state = geography.state AND orders.country = geography.country AND orders.region = geography.region;
